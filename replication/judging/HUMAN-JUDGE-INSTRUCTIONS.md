# Instructions for human judges

Thank you for helping. This page is for people. You don't need to write code, upload files, or know anything about the models.

## What the study is

The Irreducibly Human Work Lexicon is a dictionary of the things job postings and courses ask for: skills, tools, knowledge areas, abilities, languages and credentials. Several AI models each wrote their **own** version of the dictionary, without seeing the others. We want to know how far they agree, and agreement has to mean **in meaning**, not in wording.

AI judges do most of the comparing. **Your job is to tell us whether the AI judges can be trusted.** You'll see pairs of entries side by side, written by models you won't be told the names of, and say how their meanings relate. We then compare your answers with the AI judges' answers, and with other people's.

There are no right answers we're hoping for. An honest "I'm not sure" is far more useful than a guess.

## How much time it takes

- About **100 items**, or **50** if you prefer. Most take one to two minutes, so plan on about **3 to 5 hours in total**, split into as many sittings as you like.
- About a third of your items are also shown to other judges, so we can see how far people agree with each other. The rest are yours alone. Your sample is drawn at random for you.

## How to start

1. Open **Claude Code** or **Codex** in a copy of this repository (Bear will send the link and the run folder name).
2. Type: **"I'm a human judge."**
3. The assistant asks your name and an id (for example `human-jsmith`), and whether you want 100 items or 50. It then draws your sample.
4. It shows you **one item at a time**. Answer in your own words, as you would to a colleague: "B is just a narrower version of A", say, or "these are about completely different things". The assistant turns that into one of the labels below, **reads it back to you**, and saves it only when you confirm. Your own words are saved alongside, exactly as you said them.
5. When you finish, or whenever you stop, it checks your answers and saves them under your name.

The assistant will not suggest an answer before you have given yours. If it seems to, tell it to stop.

## Pausing and resuming

- Say **"pause"** at any time. Everything you have confirmed is saved.
- To resume, open Claude Code or Codex in the repository again and say **"I'm a human judge, resuming as human-jsmith"** (with your id). It picks up at your next unanswered item.
- You can change an earlier answer: say "go back to item 12".

## The labels, with worked examples

Most items show **two definitions** of the same concept, labelled A and B. Pick the relation between their **meanings**:

| Label | Meaning | Worked example |
|---|---|---|
| **Equivalent** | Same thing, same essentials. Either could replace the other. | *Python.* A: "A general-purpose programming language known for readable syntax, used for scripting, data analysis and web back ends." B: "A widely used high-level language for writing software, popular in data work and automation." |
| **A narrower** or **B narrower** | Same thing, but one covers strictly less. | *Statistics.* A: "Collecting, analysing and interpreting numerical data to draw conclusions." B: "Using hypothesis tests to check whether results are significant." **B narrower.** |
| **Overlapping** | Same thing, different emphasis. Neither contains the other, and nothing contradicts. | *Teamwork.* A: "Working with colleagues toward shared goals." B: "Communicating openly and sharing responsibility within a group." |
| **Conflicting** | Same thing, but they contradict each other on a fact. | *PostgreSQL.* A: "An open-source relational database system." B: "A dialect of the SQL language." A database system is not a language. |
| **Different sense** | They're about different things. | *Service orientation.* A: "Actively looking for ways to help customers and colleagues." B: "A software design approach built from loosely coupled services." |
| **Not sure** | You can't tell, or you don't know the concept well enough. | Use it freely. It is counted as "no answer", not as a wrong answer. |

Some items ask something slightly different. The assistant explains each kind when it first comes up:

- **Same sense?** Several short statements of what a concept means. Which ones are about the same thing?
- **Same name?** A list of alternative names (for example "Golang", "Go language") or related concepts. Which ones name the same thing? Something broader or narrower is **not** the same thing: Java is not Java EE.
- **Relation type.** Two models link the concept to the same other concept in different ways (for example "PostgreSQL is a kind of SQL" against "PostgreSQL uses SQL"). Are those the same kind of link, compatible ones, reversed (one says "kind of", the other "has kinds"), or in conflict?

## A few tips

- Judge **meaning**, not writing quality. A longer or more polished definition is not more correct.
- Don't look things up to decide which one is *right*. We only ask whether they *agree*. (Looking up a term you don't know at all is fine, and so is "Not sure".)
- Don't talk with other judges about specific items until everyone has finished.

## Your answers and your name

Your answers are saved in the repository under your id, together with your name as the author, so your contribution is credited. Your comments are stored word for word. If you would rather be credited by initials only, tell the assistant at the start.
