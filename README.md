# project3-social-fitness(https://github.com/Louiseskinner01/project3-social-fitness)

Developer: Louise Skinner ([Louiseskinner01](https://www.github.com/Louiseskinner01))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Louiseskinner01/project3-social-fitness)](https://www.github.com/Louiseskinner01/project3-social-fitness/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Louiseskinner01/project3-social-fitness)](https://www.github.com/Louiseskinner01/project3-social-fitness/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Louiseskinner01/project3-social-fitness)](https://www.github.com/Louiseskinner01/project3-social-fitness)
[![badge](https://img.shields.io/badge/deployment-GitHub Pages-purple)](https://louiseskinner01.github.io/project3-social-fitness)

## Social Fitness
Social Fitness is a community-driven web application designed to motivate users through social interaction and workout tracking. The platform allows users to create an account, share workout posts with images, specify workout type and intensity, and engage with other users through likes and comments.

The application focuses on simplicity, accessibility, and accountability, providing a space where users can document their fitness journey, interact with a supportive community, and manage their own content through personalised profiles.

**Site Mockups**
![screenshot](documentation/images/site-mockup.png)

source: [project3-social-fitness amiresponsive](https://ui.dev/amiresponsive?url=https://louiseskinner01.github.io/project3-social-fitness)

### The 5 Planes of UX
#### 1. Strategy

**Purpose**
- Provide users with a clean and simple web application where they can engage and socialise with others users on their fitness journey.
- Deliver a tool where users can upload and delete images, create and edit comments and like an unlike posts.
- Support accessibility through clear design, responsive layouts, and intuitive controls.

**Primary User Needs**
- Create POSTS which can be visible to other users via a main social feed page.
- Track a personal fitness journey and engage with others to feel motivated and inspired.
- Enjoy a social-media like experience specifically for individuals on a fitness journey.

**Site Owner Goals**
- Provide a simple and accessible social fitness platform.
- Encourage community engagement.
- Enable content management and moderation.
-Demonstrate full-stack development capability.
#### 2. Scope

**[Features](#features)** (see below)
- User registration and authentication.
- Create, edit and delete posts.
- Upload workout images.
- Add workout type and intensity.
- Like/unlike posts.
- View personal profile.
- Responsive navigation.


**Content Requirements**
- Comments and likes
- User-generate workout posts
- Profile-specific content
- Static informational pages (landing (home) & index(social feed)


#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
   - Navigation Menu: A dynamic nav bar that displays different nav links depending on whether the user is logged in or not. If the user is not logged in/signed up they will see the following links: Home, Social Feed, Login and Signup. If the user is logged in they will see: Social Feed, My Profile and Logout (NOTE: if the user is on My Profile they will also see a nav link called Create Post)

**User Flow**
  - Landing page accessible to all users.
  - Authentication redirects users to the social feed.
  - Profile page allows users to manage their own content.
  - Posts display chronologically.
  - Comments nested beneath posts. 
  - Conditional navigation links based on login state


#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

The visual design of Social Fitness follows a minimal and content-focused approach. The design philosophy aligns with modern social platforms where simplicity and clarity enhance user engagement whilst adopting a cleaner and more neutral style to support usability and readability.

Bootstrap’s default styling and component library were intentionally used to ensure visual consistency, accessibility, and responsive behaviour across devices. The design prioritises user-generated content—such as workout images and captions—rather than decorative elements, allowing posts to remain the primary focal point of the interface.
A restrained colour palette and standardised button styles were selected to reduce visual clutter, improve contrast, and maintain a professional appearance suitable for a social platform. This approach supports scalability, ensuring that additional features or user-customisation options can be integrated in future iterations without conflicting with an overly complex theme.

**Colour pallet**<br>
- Delete button (btn-danger)
- Like/unlike button ()
- Post button
- Login
- Logout

![screenshot](documentation/images/coolors-colour-theme.png)

### Typography



## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.


| Page | Mobile (landscape & portrait)  Tablet Desktop |
| --- | --- |
| Home| ![screenshot](documentation/wireframes/Home.png) |
| 404 Error | ![screenshot](documentation/wireframes/404.png) |
| Create Post | ![screenshot](documentation/wireframes/create-post.png) | 
| Login | ![screenshot](documentation/wireframes/login.png) | 
| My Profile | ![screenshot](documentation/wireframes/my-profile.png) |
| Sign up | ![screenshot](documentation/wireframes/sign-up.png) | 
| Social Feed | ![screenshot](documentation/wireframes/social-feed.png) |


## User Stories
### General Play

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a user | I would like to upload a image | so that I can populate my profile page with images of my workouts. |
| As a user | I want add a caption | so that my posts can be accompanied by a description. |
| As a user | I would like to add a workout type and an intensity level | to give more meaning to my workout post. |
| As a user | I would like to create an account | so I can use the social-fitness platform. |
| As a user | I would like to log in and out out of my account | so my profile is kept safe from non-authenticated users. |
| As a user | I would like to be able to delete my post | so I have full control of my user profile and what is and isnt displayed. |
| As a user | I would like like to view the main social feed | so I can be inspired by other users. |
| As a user |  I would like to like posts that other users have posted on the main social feed | so that I can share my interests. |
| As a user | I would like to comment on other users posts  | so that I can share my thoughts. |
|As a user | I want to be able to edit a comment I have made | so my comment can be corrected if I have made a mistake.|
|As a user | I want to access to to simple and clean navbar | so I can easily navigate through the web apps pages. |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. |


### Accessibility & Usability

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a visually impaired user | I want clear colour contrasts (e.g. bold backgrounds and bright highlights) | so that I can see buttons and numbers more clearly. |
| As a user with little computer skills | I want a simple web app | so I can fully utilise the apps features. |
| As a mobile user | I want large, tap-friendly buttons | so that I can use the app easily on my phone. |

### Content & Motivation 

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a casual user | I want to be able to share my workouts | so that I can enjoy the web application without pressure. |
| As a competitive user (fitness influencer)| I want to sutilise the app | so that I can inspire other users who are new to fitness. |
| As a user new to fintess | I want to be able to access a community | so that I can learn and be inspired by fitness content. |
