# job-board-platform

## What it is
This is a web application that allows anyone to create their own job board. You can think of it as a Shopify for job boards. 

## Why I built it
In early 2021 I noticed that a lot of people were hosting job boards. These were typically influencers, writers, or people with large Twitter followings. They would host a web page with a list jobs relevant to their community. Companies would pay to post listing on these boards. I noticed that all of these job boards were put together from scratch. Some coded their own, others used no-code tools or website builders. Companies had to submit jobs through sketchy forms or email.

The idea behind this MVP was to create a platform for job boards. Creators would easily be able to generate a job board. Employers would easily be able to submit jobs. Both the board's host and companies would have access to dashboards to manage their listings and keep track of performance. 

## Features
As a host, I can
- Create an account and a job board which anyone can view
- Access a host dashboard where I can:
  - Add, edit, or remove listing from my job board
  - See how many times my board, and each individual job, has been viewed
  - Review, accept, or deny pending job posts from employers

As a user looking for jobs, I can
- View a job board that is shared with me and browse the postings within that board

As an employer, I can
- Submit jobs to a board
- View an employer dashboard in which I can: 
  - View, update, and delete my listings
  - Check the status of pending listings that I have submitted
  - See how many views my listing have

## Technologies
This was built entirely with Django on the backend. It runs on a PostgreSQL database. It is HTML, CSS, and Bootstrap on the frontend. 

Building this involved a number of interesting technical challenges including:
- Implementing a way to count hits of a page or post
- Implementing a system where employers could submit a post for review
- Writing views and querysets such that I could display information from multiple database models on one page (i.e. host information and job list)

## Future work
I put this project down after a month of part time work. Around the same time, a platform called [Pallet](https://lennys-jobs.pallet.com/jobs) took off. Pallet does everything this app was intended to do and much more. I was actually able to chat with the founder, which was really inspiring. 

If I was to continue working on this, there's a number of things I would work on
- Adding built in payments beween hosts and employers
- UI improvements
  - A strong UI would help attract people looking for jobs to the platform, and increase legitimacy on the employer side. 
- I would consider rebuilding this with a serarate React frontend and Django backend. As the number of pages, and complexity of each began to scale, working on a monolith became painful. In order to scale well, I think it would make sense to separate the frontend and backend. This would also allow me to utilize React components to manage frontend complexity.

## Learnings and reflections
This was a fun project to work on. Most valuably, I saw that I could conceptualize and build something with potential to address a real problem (as evidenced by Pallet's succcess). I also learned to think about web applications at the system level - considering how different models, views, and parts would work together. Working on this by myself gave me appreciation for team work in software and why working in groups is super power when it comes to building complex applications.

