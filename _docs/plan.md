# Weekly Project Feedback Tool — Product Scope

## Product Goal
Build a weekly project feedback tool for teams where all team members can submit structured feedback on project progress, tasks/features, collaboration, blockers, and risks.

The tool should encourage regular feedback while keeping participation flexible, transparent, and lightweight.

---

## 1. Users and Roles

### Primary Users
- All team members

### Roles
- Owner
- Admin
- Member

### Permissions
- Owners and Admins can:
  - Remove members
  - Change member roles
  - Change project settings
  - Change project name
  - Change weekly deadline
  - Disable or regenerate invite links
  - View submission status for team members
  - Send manual reminders to people who have not responded

- Members cannot:
  - Remove members
  - Change roles
  - Change project settings

---

## 2. Project Membership

### Joining a Project
- Users join through a shareable invite link.
- Anyone with the active invite link can join directly.
- No approval is required.

### Invite Link Controls
- Owners/Admins can:
  - Disable the invite link
  - Regenerate a new invite link

---

## 3. Project Status

Projects can have one of three statuses:

- Active
- Paused
- Archived

### Paused Projects
- Weekly reminders stop.
- Team members can still submit feedback.
- Existing feedback can still be edited and discussed.

### Archived Projects
- Users can still:
  - Submit/edit feedback
  - Reply
  - React
  - Use @mentions
- Archived projects still send notifications for:
  - Replies
  - Reactions
  - @mentions

---

## 4. Weekly Feedback Structure

### Core Feedback Areas
Every project uses the same fixed core sections every week:

- Overall project progress
- Specific tasks/features
- Team collaboration
- Blockers
- Risks

### Core Questions
- The full fixed set is shown every week.
- Core sections cannot be turned off per project.

### Custom Questions
- Projects can also have optional custom questions.
- Any team member can add a custom question.
- Custom questions become active immediately.

---

## 5. Ratings and Comments

### Rating System
- 1–5 stars

### Requirements
- Star rating is required.
- Written comment is optional.

---

## 6. Identity and Anonymous Feedback

### Default Behavior
- Feedback is named by default.

### Anonymous Option
- Contributors can choose to submit feedback anonymously.
- Anonymous means fully anonymous to everyone.
- Owners and Admins cannot see the contributor identity.
- Anonymous identity is not revealed in exports.

### Changing Identity
- Users can switch submitted feedback between:
  - Named
  - Anonymous

### Anonymous Feedback Interaction
Anonymous feedback supports the same features as named feedback:

- Replies
- Reactions
- @mentions

---

## 7. Feedback Visibility

- Submitted feedback is visible to the whole team immediately.
- Feedback does not wait until the weekly deadline to become visible.

---

## 8. Editing and Deleting Feedback

Users can:

- Edit their submitted feedback
- Delete their submitted feedback

### Edited Feedback
- Edited feedback shows an `Edited` label.
- Full edit history is not shown.

---

## 9. Replies

- Team members can reply to feedback.
- Replies are simple replies only.
- No deep/nested threaded conversations.

---

## 10. Reactions

Users can react to feedback.

### Reaction Rules
- Reactions use a small fixed set of emoji.
- Users cannot choose any arbitrary emoji.
- Users can see who reacted.

Example reaction set:

- 👍
- ✅
- 👀

---

## 11. Mentions

- Users can @mention teammates in:
  - Feedback
  - Replies

### Mention Notifications
- @mentions trigger an immediate notification.

---

## 12. Notifications

Users receive notifications when:

- Someone @mentions them
- Someone replies to their feedback
- Someone reacts to their feedback

### Notification Timing
- These notifications are immediate.

---

## 13. Weekly Deadline

### Deadline Configuration
- Each project has its own configurable weekly deadline.

### Late Feedback
- Feedback can still be submitted after the deadline.
- Late feedback is marked `Late`.

---

## 14. Weekly Reminders

### Automatic Weekly Reminder
- Everyone gets a weekly reminder.
- The reminder is sent even if the user has already submitted.
- Weekly reminders are sent by email.
- The email includes a direct link to the project's feedback form.

### Manual Reminders
- Owners/Admins can manually remind people who have not responded.
- Manual reminders are sent by email only.

---

## 15. Weekly Completion

Users can mark a project as:

`No feedback this week`

### Rules
- No reason is required.
- It counts as completed for that week.
- Users can undo the skip.
- Users can later submit feedback during the same week.

---

## 16. Drafts

Users can save unfinished weekly feedback.

### Draft Behavior
- Drafts auto-save while the user types.
- Users can return later and continue.

---

## 17. Submission Status

### Visibility
Only Owners/Admins can see who has:

- Submitted
- Skipped
- Not responded yet

Regular members cannot see team-wide submission status.

---

## 18. Feedback Feed

### Primary Organization
The project feedback feed is organized primarily by:

- Topic/question

### Filters
Users can filter feedback by:

- Week
- Person
- Anonymous vs named
- Rating

---

## 19. Search

Users can search across the project.

Search includes:

- Original feedback
- Replies

---

## 20. Dashboard

Each user has a personal dashboard.

### Dashboard Shows
- All projects the user belongs to
- Whether feedback has been completed for the current week
- Upcoming project deadlines
- Weekly completion indicator

Example:

`3 of 5 projects completed this week`

### Dashboard Controls
Users can sort projects by:

- Deadline
- Name
- Recent activity

Users can also:

- Pin projects
- Favorite projects

Pinned/favorited projects stay easy to access.

---

## 21. Exporting Feedback

Users can export project feedback as:

- CSV
- PDF

### Export Rules
- Export includes all project feedback.
- Users cannot filter exports before exporting.
- Anonymous feedback remains anonymous in exports.

---

## 22. Authentication

Users must log in before submitting feedback.

### Supported Login Methods
- Email + password
- Social login

Initial social login options can include:

- Google
- Microsoft

---

## 23. MVP Behavior Summary

A typical weekly flow:

1. A user logs in.
2. They see their projects and upcoming deadlines.
3. They open a project.
4. They complete the fixed weekly feedback questions.
5. Each question requires a 1–5 star rating.
6. Written comments are optional.
7. They can submit as themselves or anonymously.
8. Feedback becomes visible immediately.
9. Other team members can reply, react, and @mention people.
10. Feedback can be edited or deleted later.
11. Late submissions remain allowed and are marked `Late`.
12. A user may instead select `No feedback this week`.
13. Owners/Admins can see who has responded and send reminder emails.

---

## 24. Current MVP Feature List

### Authentication
- Email/password login
- Social login

### Projects
- Create/manage projects
- Active/Paused/Archived status
- Shareable invite link
- Owner/Admin/Member roles
- Configurable weekly deadline

### Feedback
- Fixed weekly feedback template
- Optional custom questions
- 1–5 star ratings
- Optional comments
- Anonymous/named submissions
- Edit/delete
- Late label
- Draft auto-save
- Skip week option

### Collaboration
- Simple replies
- Fixed emoji reactions
- @mentions
- Immediate notifications

### Discovery
- Topic-based feed
- Filters
- Full project search
- Search replies

### Dashboard
- Project list
- Submission status
- Deadlines
- Completion indicator
- Sorting
- Pin/favorite

### Email
- Weekly reminders
- Manual reminder emails
- Direct feedback-form links

### Export
- CSV
- PDF

---

## 25. Decisions Still Open

The following areas have not yet been scoped:

- Exact fixed weekly questions
- Exact fixed emoji reaction set
- Social login providers beyond Google/Microsoft
- Project creation flow
- Whether anyone can create a project
- Whether there are organization/workspace-level accounts
- Email notification preferences
- In-app notification center design
- Whether replies can be edited/deleted
- Whether custom questions can be edited/deleted
- Question ordering
- Whether questions support categories/tags
- File/image attachments
- Mobile app vs responsive web only
- Analytics/reporting
- Data retention
- Security/audit requirements
- Pricing and billing
- Admin moderation/reporting
- Technical architecture
- MVP vs post-MVP prioritization
