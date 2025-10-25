<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Purpose](#purpose)
- [1. Person Schema](#1-person-schema)
- [2. Creating a Person](#2-creating-a-person)
- [3. Editing a Person](#3-editing-a-person)
- [4. Assigning Roles](#4-assigning-roles)
- [5. Connections](#5-connections)
- [6. Storage & Persistence](#6-storage--persistence)
- [7. Future Integration (not yet implemented)](#7-future-integration-not-yet-implemented)
- [8. Next Steps](#8-next-steps)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Purpose

The People section manages **individuals relevant to a project**.
Each project may involve different people. The system requests basic information (at least a name), with optional fields (DOB, role, notes, etc.) on a **per-case basis**.

Once created, people can later be linked as:

- Speakers in transcripts
- Participants in A/V files
- Mentioned individuals in PDFs
- Filters in Views (e.g., "show only statements involving Person X")

This document defines:

1. Data schema for a `Person` object.
2. Rules for creating, editing, and saving people in a project.
3. Future hooks for linking people into other modules.

---

## 1. Person Schema

Each person is represented as a JSON object in the project's people store.
The actual information sought or stored is flexible, but the wizard for creating a person requires at least a last name. The rest is addressed per PR28

```json
{
  "id": "uuid-or-slug",
  "fullName": {
    "last": "Doe",
    "first": "John",
    "middle": "A",
    "suffix": "Jr."
  },
  "title": "Mr.",
  "pleadingName": "John Doe",
  "aliases": ["Johnny", "JD"],
  "dateOfBirth": "1985-06-01",
  "age": 39,
  "contacts": {
    "phones": [
      { "type": "mobile", "number": "555-123-4567" },
      { "type": "home", "number": "555-987-6543" }
    ],
    "social": [{ "handle": "@johnny", "platform": "twitter" }]
  },
  "docNumbers": [{ "state": "MI", "number": "123456" }],
  "roles": [
    { "category": "Defendant", "caseSpecific": true },
    { "category": "Witness", "subtype": "Eyewitness", "caseSpecific": true }
  ],
  "connections": [
    { "to": "person-id-2", "type": "friend" },
    { "to": "person-id-3", "type": "attorney" }
  ],
  "notes": "Known to be involved in 2018 incident, moved to another state."
}
```

**Key points**:

- `id`: stable identifier (UUID or slug).
- `roles`: multiple roles allowed, can be flagged `caseSpecific`.
- `connections`: explicit links between people.
- `notes`: arbitrary text (reminders, significance, context).

---

## 2. Creating a Person

- **Required:** `fullName` (at least `last`, optionally `first`).
- **Optional:** Any other field.
- Person is saved into `projectRoot/people/people.json`.

**Workflow**:

1. User clicks **"Add Person"**.
2. Minimal form asks:

   - Last Name (required)
   - First Name (optional)
   - Role (optional, can add later)

3. After save, system generates `id`.
4. User can expand/edit person record later with full details.

---

## 3. Editing a Person

- Click on a person's name to open **detail form**.
- All fields editable (DOB, aliases, contacts, roles, connections).
- Changes are saved back to `people.json`.
- Keep an **edit history** (optional future feature).

---

## 4. Assigning Roles

- Roles are **not hardcoded**.
- Base role categories provided (Defendant, Victim, Witness, Informant, Expert, Law Enforcement, Prosecutor, Defense Attorney, Judge).
- Each can take **subfields**:

  - Witness → {Eyewitness, Alibi, Expert, Other}
  - Expert → {field, employer, side (P/D)}
  - Law Enforcement → {department, badge, rank, role in investigation}

- User can add **custom/free-text role** if needed.

---

## 5. Connections

- Each person can be linked to others with a `connection`.
- Predefined types: parent, sibling, spouse, partner, child, coworker, friend, attorney, law enforcement, prosecutor, judge, expert.
- Free text allowed if none fits.
- Connections stored as `{to: person-id, type: "friend"}`.

---

## 6. Storage & Persistence

- **Project scope:** People are saved under each project.
- **File layout:**

  ```
  projectRoot/
    people/
      people.json   ← master store of Person objects
      connections.json (optional if separated later)
  ```

- **Format:** JSON array of `Person` objects.
- **Example:**

  ```json
  [
    {
      "id": "john-doe",
      "fullName": { "last": "Doe", "first": "John" },
      "roles": []
    },
    {
      "id": "jane-doe",
      "fullName": { "last": "Doe", "first": "Jane" },
      "roles": []
    }
  ]
  ```

---

## 7. Future Integration (not yet implemented)

- **Transcripts:** assign person as speaker.
- **A/V files:** tag participants.
- **PDFs:** link mentions to people.
- **Views:** filter statements by person(s).
- **Search/Filter:** "show me everything involving John Doe."

---

## 8. Next Steps

- ✅ Define JSON schema (done).
- 🔲 Implement "Add Person" form (with minimal required fields).
- 🔲 Implement "Edit Person" detail panel.
- 🔲 Save all people to `people.json`.
- 🔲 Hook into transcript speaker assignment.
- 🔲 Enable view filtering by person.
