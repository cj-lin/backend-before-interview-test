# Schema Design

We plan to design and develop a resume management system (RMS).

System will have many users and they will have different role (permission) in this system.

The main module of RMS is resume maintenance.

Each user can have many resumes in RMS, each resume can maintain different work experience and **autobiography**.

Each resume can have many templates for showing different style with same information.

Below are samples for some different template.

Please design schema (table and column) for the RMS.

Include PK, FK, Index , Constraint, Relation for the schema.

You can use Excel, ERD Diagram or UML Diagram to show your design, but it’s important to

let us know the relationship between tables.

## Use Case 1：

Davis is a candidate, he has two resumes (A, B) in RMS.

Resume A has two templates (A1, A2).

Resume B has one template (B1).

## Use Case 2：

Alan is a hunter, he will login RMS for searching candidate.

He wants to find a list for who has five-experiences in the same company.

List has three columns: name, company, experience-year

Sample: Davis, MorrisonExpress, 5

## Submission

SQL file and ER diagram are provided. All FK naming rule is identical: *table_column*.
