title: Besuch der DjangoCon Europe 2012 in Zürich
duration: Juni 2012
tags: [ Django, ]
date: 2012-06-01 12:00
---
> DjangoCon Europe is the main conference for development of and with the Django Framework in Europe.

The presentations I liked:

* PostgreSQL when it is not your job.
  by Christophe Pettus
  In this DevOps world, Django programmers are increasingly being asked to manage the database as well.
  In 45 brisk minutes, we will talk about (nearly) everything you need to know to bring up, tune, and keep a PostgreSQL database health.
  We'll go over installation, basic tuning, backups, disaster recovery, and helpful tools and techniques.
* Django and the Real-time Web
  by Zachary Voase
  The modern Web—indeed, the modern user—demands that we write applications that work faster than the traditional request/response cycle.
  But how relevant is Django in the age of pjax, node.js and WebSockets?
  I believe Django remains a powerful utility in the new Web, and in this talk I'll share some techniques and tools for reducing the complexity of real-time applications.
  I'll explain how I manage code duplication when key business logic is split between the client and the server, and demonstrate ways to preserve a RESTful and accessible design whilst providing a more responsive experience to clients who support it.
  Technologies I'll touch upon include ZeroMQ, gevent and WebSockets, and I hope to leave everyone from beginner to veteran with some valuable insights.
* Building secure Django websites
  by Erik Romijn
  Django helps web developers in many ways, security included. But, it can't and won't handle everything - there's still security issues left that you need to take care of yourself.
  This talk explores some of the most common security issues Django developers can face, with a specific focus on using the features Django already provides to help out. We'll look at how vulnerabilities can be exploited, how exactly Django tries to help and what you still need to take care of yourself.
* I Hate Your Database
  by Andrew Godwin
  After years of working with all sorts of databases and wrangling with South to support just five of them, Andrew takes a look at databases (relational, document, key-value and more) and at some of the problems that Django programmers often come across with them.
  The talk will cover (among other things) the disadvantages of relational databases, why "NoSQL" isn't always the answer, the pains of storing geographic data, a small amount of database theory, and the very small number of good things about MySQL.
* It's about time!
  by Aymeric Augustin
  Time zone support is a major new feature in Django 1.4, but empirical evidence shows it's often overlooked or misunderstood.
  This talk explores how dates and times are represented in Python, why their handling was overhauled in Django, and what it means for developers.
* Adding Tests to an Uncovered Application
  by Zach Smith
  Ideally, all code would have test coverage, but this is not a reality.
  When you start a new project, you want to move as quickly as possible. This often comes at the expense of test coverage. Besides, you don't even know if anyone will even use your application, so tests might never be necessary.
  As your userbase and your team grow, however, testing becomes a necessity.
  This talk will go over tools and strategies employed by Yipit in transitioning from a 3 person development team working on an application with no tests, to an organization of 14 engineers with a highly covered codebase.
* Flasky Goodness (or Why Django Sucks?)
  by Kenneth Reitz
  This talk dives into the specifics of why Django isn't always the best tool for the job, general frustrations with the framework, and potential fixes.