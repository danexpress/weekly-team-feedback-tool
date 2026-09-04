# Weekly Team Feedback Tool — MVP Backlog

Tasks are ordered roughly in build sequence but each one is written to
stand alone: a contributor should be able to pick up a single task
without having read the others. Architecture assumed: a React/Vite
frontend, a separate backend API, a separate AI worker service, Postgres,
and Redis for the job queue (Option D from the tech stack discussion).

## 1. Project scaffolding with a passing test
Goal: Stand up empty frontend, API, and AI worker projects with one passing test each.
Description: Create the initial repo structure (a monorepo with `frontend/`, `api/`, and `worker/` packages is fine) with dependencies, a test runner, and linting configured for each. Add one trivial passing test per package (e.g., a health-check test) and a CI workflow that runs all three on push, so the pipeline is proven before any real feature work begins.

## 2. Postgres schema for users and projects
Goal: Define the initial relational schema for users, projects, and membership.
Description: Set up Postgres with a migration tool and create the first migration covering `users`, `projects`, and `project_members` (with a role column for team member/facilitator). Include a local seed script with a couple of sample users and one project.

## 3. User authentication (signup and login)
Goal: Let a user create an account and log in.
Description: Implement email/password (or magic-link) authentication in the API, issuing a session token the frontend can store and send on later requests. Include tests for successful signup, successful login, and rejection of invalid credentials.

## 4. Role-based authorization middleware
Goal: Restrict facilitator-only actions to users with the facilitator role.
Description: Add middleware/guards to the API that check a user's role on a given project before allowing actions such as starting a retrospective or revealing feedback. Add a test asserting a non-facilitator request is rejected with the correct error.

## 5. Project creation and listing
Goal: Allow creating a project and viewing the projects a user belongs to.
Description: Implement API endpoints and a minimal frontend page to create a project and list the projects the logged-in user is a member of. A single project's detail page can be a placeholder for now, showing just its name and member list.

## 6. Invite a team member to a project
Goal: Let a facilitator add an existing user to a project.
Description: Add an endpoint and simple UI for adding a user (by email) to a project's member list with a default "team member" role. Assume the invited person already has an account — onboarding brand-new users is out of scope for this task.

## 7. Feedback cycle creation
Goal: Let a facilitator start a new weekly feedback cycle for a project.
Description: Implement an endpoint and UI action to create a feedback cycle under a project, with a status field (e.g., collecting/revealed/closed) and a start date. A project should be able to report its current open cycle, if any.

## 8. Feedback card submission (Start/Stop/Continue)
Goal: Let a team member submit short feedback cards under a cycle.
Description: Build the feedback form with three sections — Start, Stop, Continue — where a user can add multiple short text cards. Store each card with its category, author, and cycle reference, and let the author edit or delete their own cards while the cycle is still collecting.

## 9. Anonymous submission flag per card
Goal: Let a contributor mark an individual card as anonymous.
Description: Add an "anonymous" checkbox per card that, when set, excludes the author from all API responses except where needed to authorize the author's own edits. Add a test confirming an anonymous card's author is never exposed to other users, including facilitators.

## 10. Enforce private feedback before reveal
Goal: Ensure contributors can only see their own cards until the cycle is revealed.
Description: Add authorization logic so that fetching a cycle's cards returns only the requesting user's own cards while the cycle is "collecting," and all cards (respecting anonymity) once it becomes "revealed." Cover both states with tests.

## 11. Facilitator reveal action
Goal: Let a facilitator reveal all submitted feedback for a cycle at once.
Description: Add an endpoint that transitions a cycle from "collecting" to "revealed," after which all team members can see all cards. Restrict this action to the facilitator role and test that others are rejected.

## 12. Manual cluster management
Goal: Let the team organize revealed cards into clusters by hand.
Description: Implement a `clusters` table and endpoints to create a cluster, assign a card to it, move a card between clusters, rename a cluster, and merge two clusters into one. Cards with no assigned cluster should remain queryable as "ungrouped."

## 13. Automatic clustering suggestion
Goal: Propose starter clusters for the team to refine after reveal.
Description: Implement a first-pass clustering step that runs when a cycle is revealed and proposes initial clusters for the cards (a simple similarity heuristic is enough for a first version — it does not need to call an LLM). The team then edits these using the tools from the manual clustering task, so this task only needs to produce a reasonable starting point.

## 14. Cast and update votes
Goal: Let each team member allocate up to 3 votes across clusters.
Description: Implement an endpoint that lets a user place, move, or remove votes (up to 3 total, stackable on a single cluster) on the clusters of a retrospective. Enforce the 3-vote cap server-side and add a test for the boundary case (attempting a 4th vote).

## 15. Vote visibility rules
Goal: Hide vote totals from participants until voting closes.
Description: Ensure vote counts are omitted from API responses while a retrospective is in "voting" status, and included once the facilitator closes voting (or once everyone has voted). Add tests covering both states.

## 16. Prioritized discussion agenda
Goal: Produce a ranked list of clusters to discuss once voting closes.
Description: Add an endpoint that returns a retrospective's clusters ordered by total vote count after voting has closed, to drive the discussion queue on the retrospective board.

## 17. Discussion status tracking
Goal: Let the facilitator record the outcome of each discussion topic.
Description: Add a status field (Discussed / Skipped / Deferred) on each cluster within a retrospective, with an update endpoint restricted to the facilitator role, used as the meeting progresses through the agenda.

## 18. Manual notes and action items during discussion
Goal: Let attendees record notes and action items live during the meeting.
Description: Add a notes field per discussion topic and an `action_items` table (description, owner, optional due date, status, related topic) with endpoints to create and edit entries by hand, independent of the later AI-extraction pipeline.

## 19. Realtime updates for the retrospective board
Goal: Push live updates to everyone viewing an active retrospective.
Description: Add a WebSocket gateway (e.g., Socket.io backed by Redis pub/sub) that broadcasts reveal, cluster-change, vote-closed, and discussion-status events to connected clients on that retrospective, and update the frontend board from these events instead of polling.

## 20. Meeting record upload
Goal: Let a facilitator upload an audio file, video file, transcript file, or pasted transcript text.
Description: Implement an upload endpoint that accepts the four input types, stores any files in S3-compatible object storage, and creates a `meeting_upload` record with a status field (pending/processing/done/failed) for tracking downstream processing.

## 21. Job queue between the API and the AI worker
Goal: Wire up asynchronous processing between the API and the separate AI worker service.
Description: Set up a message queue (e.g., Redis with BullMQ, or RabbitMQ) so the API enqueues a job when a meeting upload finishes, and the AI worker service consumes it. Implement one no-op job end-to-end (enqueue → worker logs receipt → marks upload "processing") to prove the pipeline before adding real AI logic.

## 22. Transcription step in the AI worker
Goal: Produce a text transcript from an uploaded audio or video file.
Description: In the AI worker, add a processing step that calls a transcription API for audio/video uploads, and passes through the provided text directly for transcript-file or pasted-text uploads. Store the resulting transcript on the `meeting_upload` record and update its status.

## 23. Extraction step in the AI worker
Goal: Generate draft decisions, action items, and a summary from a transcript.
Description: Add a processing step that sends the transcript to an LLM to produce draft decisions, action items (with owner and due date when mentioned), and a short retrospective summary, storing these as unconfirmed/draft records linked to the meeting upload.

## 24. Facilitator review and approval of AI drafts
Goal: Let the facilitator confirm or edit AI-suggested outcomes before they become official.
Description: Build a review screen listing the AI-drafted decisions and action items, letting the facilitator edit, discard, or confirm each one. Only confirmed items should be written into the retrospective's real decisions and `action_items` records.

## 25. Retrospective summary and publish
Goal: Show the final record of a completed retrospective and lock it.
Description: Build a read-only summary view containing top discussion topics, key notes, confirmed decisions, confirmed action items, attendance/participation, and the original feedback cards. Add a "publish" action, restricted to the facilitator, that marks the retrospective as complete.

## 26. Project dashboard page
Goal: Give a project's home page a useful at-a-glance overview.
Description: Build the project page showing the current feedback cycle and submission status, the upcoming or active retrospective, a list of previous retrospectives, and the project's currently open action items.

## 27. Action item status updates by owner
Goal: Let a user mark their assigned action items as done.
Description: Add an endpoint and a small UI control so a user can toggle the status (Open/Done) of action items assigned to them, independent of which retrospective the item originated from.

## 28. Deployment configuration for all services
Goal: Make the frontend, API, and AI worker deployable outside a local dev machine.
Description: Write Dockerfiles (or equivalent) and a docker-compose file (or basic deployment scripts) for the frontend, API, worker, Postgres, and Redis, so the whole system can be run and smoke-tested as a deployed environment.
