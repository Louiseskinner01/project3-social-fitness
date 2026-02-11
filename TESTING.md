# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Rationale

The primary goal of testing was to ensure that the Social Fitness application performs consistently across multiple devices and screen sizes, maintaining both functionality and a smooth user experience.
Testing focused on performance, accessibility, and responsiveness.

## Approach
Testing was carried out to verify that the website functions as intended, is fully responsive, and provides an intuitive user experience.
All tests were conducted manually using a combination of Google Chrome DevTools, validation tools, and live user interaction testing.

## Methods

| Method                    | Description                                                                                                                                                                        | Tools Used                                                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Manual Testing**        | Each feature and button was manually tested to verify correct functionality. This included checking form submissions, button click responses, login/signup authentication and image upload. |  Google Chrome                                                                                                  |
| **Responsive Testing**    | Tested using Chrome DevTools’ built-in device emulation. Ensured the layout adapts correctly to different screen widths and orientations.                                          | Chrome DevTools                                                                                                                           |
| **Cross-Browser Compatability Testing** | Tested in multiple browsers to ensure consistent design, color rendering, and interactivity.                                                                                       | Chrome, Firefox, Safari, Edge                                                                                                     |
| **Validation Testing**    | Used validation tools to check that the HTML and CSS are free from syntax errors and follow best practices.                                                           | [W3C HTML Validator](https://validator.w3.org/), [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) |
| **Accessibility Testing** | Checked color contrast, font readability, tab navigation, and proper use of ARIA and semantic tags where applicable.                                                               | Chrome Lighthouse, manual checks                                                                                                          |
| **Performance Testing**   | Evaluated page load speed and responsiveness using Chrome Lighthouse.                                                                                                              | Chrome DevTools  Lighthouse     


### Manual Tests (Defensive Programming)


- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages


| Feature Tested | Test Description                                   | Expected Outcome                                | Pass/Fail             |  Screenshot |
| ------------------- | ------------------------------------------------ | ----------------------------------------------- | ------------------- | ----------- |
| Signup (valid) | Create a new account with valid username/password (and email if used) | Account created successfully and user is logged in / redirected | ✅ Works | ![screenshot](documentation/manual-testing/required-email.png) |
| Signup (duplicate username)	| Attempt to sign up using an existing username	| Form displays error and prevents account creation		| ✅ Works | ![screenshot]() |
| Signup (password mismatch) |	Enter two different passwords in password fields | Validation error shown and account not created | ✅ Works | ![screenshot](documentation/manual-testing/Screenpassword-mismatch.png) |	
| Signup (weak password) | Enter a weak password e.g l1 or 123 | Should display an error message stating that the password is weak and what the requirements are for a strong and successful password  | ✅ Works | ![screenshot](documentation/manual-testing/week-password.png) |	
|Brute-force URL testing | Visit restricted pages without being logged in as a aunthenticated user | Should send user to login page | ✅ Works | ![screenshot](documentation/manual-testing/brute-force1.png) <br> ![screenshot](documentation/manual-testing/brute-force2.png)|
| Navigation (Burger-icon)     | Changed the screen size to viarious sizes and also clicked on the burger icon when testing on mobile and tablet devices.   | Appears when the screen size is small and disappears (expanding into a full navigation bar) when the screen is large. | ✅ Works          | **Navbar expand** ![screenshot](documentation/manual-testing/navbar-expand.png)<br> **Navbar toggle** ![screenshot](documentation/manual-testing/navbar-toggle.png)<br> **Navbar toggle expand** ![screenshot](documentation/manual-testing/navbar-toggle-expand.png) |
| Login (valid)                       | Log in with correct username and password                        | User is authenticated and redirected to Social Feed                      |           | ![screenshot](documentation/manual-testing/login.png) |
| Login (invalid)                     | Attempt login with incorrect password                            | Error message shown and login denied                                     |           | ![screenshot](documentation/manual-testing/incorrect-password.png) |
| Logout                              | Click logout while logged in                                     | User is logged out and redirected; restricted pages no longer accessible |           | ![screenshot](documentation/manual-testing/logout.png) |
| Create post (valid)                 | Submit new post with image + caption/workout/intensity           | Post is saved and displays on Feed and Profile                           |           | ![screenshot](documentation/manual-testing/create-post1.png) <br> ![screenshot](documentation/manual-testing/create-post2.png) <br> ![screenshot](documentation/manual-testing/create-post3.png)|
| Create post (missing image)         | Submit post form without selecting an image                      | Form validation error displayed; post not created                        |           | ![screenshot](documentation/manual-testing/create-post-without-image.png) |
| Post custom fields optional         | Create post without workout/intensity                            | Post still creates successfully; optional fields remain blank            |     ✅ Works          | ![screenshot](documentation/manual-testing/custom-fields.png) |
| Delete own post                     | Delete a post created by the logged-in user                      | The user will be promted with an alert message asking if they're sure they want to delete the post. If the user confirms OK and the post is a successfully deleted, the user should be presented with an alert                       |     ✅ Works          | **Before deletion**![screenshot](documentation/manual-testing/delete0.png)<br> **Confirm deletion** ![screenshot](documentation/manual-testing/delete1.png) **Successful deletion** ![screenshot](documentation/manual-testing/delete2.png) |
| Delete other user post (defensive)  | Manually enter `/posts/<id>/delete/` for another user’s post     | Action denied (403/blocked); post remains                                |    ✅ Works           | ![screenshot](documentation/manual-testing/delete-other-user.png) |
| Add comment (valid)                 | Add a comment under a post while logged in                       | Comment saves and displays beneath the correct post                      |   ✅ Works            | ![screenshot](documentation/manual-testing/add-comment1.png) <br> ![screenshot](documentation/manual-testing/add-comment2.png)|
| Add comment (logged out)            | Try to add comment while logged out                              | User redirected to login to prevent them from commenting                    |   ✅ Works            | ![screenshot](documentation/manual-testing/login-page.png) |
| Edit own comment                    | Edit a comment created by logged-in user                         | Updated comment saves and displays correctly                             |    ✅ Works           | **Before edit**![screenshot](documentation/manual-testing/edit-comment1.png)<br> **Comment being edited** ![screenshot](documentation/manual-testing/edit-comment2.png)<br> **Comment after edit** ![screenshot](documentation/manual-testing/edit-comment3.png) |
| Edit other user comment (defensive) | Manually enter `/comments/<id>/edit/` for another user’s comment | Access denied (404/403); comment not changed                             |    ✅ Works           | ![screenshot](documentation/manual-testing/edit-other-user.png) |
| Like/unlike post                           | Click like button on a post and Prevent duplicate likes (defensive)                                      | Like is created; heart state/like count updates. Only one like per user per post (no duplicates) using toggle function                         |   ✅ Works            | ![screenshot](documentation/manual-testing/like-unlike1.png) <br> ![screenshot](documentation/manual-testing/like-unlike2.png)|
| Navbar conditional links            | Compare navbar logged out vs logged in                           | Correct links shown/hidden based on auth state                           |    ✅ Works           | **Logged out**![screenshot](documentation/manual-testing/navbar-response1.png) <br> **Logged in**![screenshot](documentation/manual-testing/navbar-response2.png) |
| Responsive images                   | View feed on small screen                                        | Images scale within container; no overflow                               |    ✅ Works           | ![screenshot](documentation/manual-testing/overflow1.png) <br> ![screenshot](documentation/manual-testing/overflow2.png)|
| Custom 404 page                     | Visit non-existent URL e.g. `/test`                              | Custom 404 page displays with correct navigation link                    |     ✅ Works          | ![screenshot](documentation/manual-testing/4042.png) |












| Element Tested                | Test Description                   | Expected Outcome                        | Pass/Fail | Screenshot |
| -------------------------- | ---------------------------------- | ----------------------------- | --------- | --------- |





| User Story Tested | Test Description | Expected Outcome | Pass/Fail |
| --- | --- | --- | --- |
| As a new user, I want to create an account so I can join the Social Fitness community |	Submit signup form with valid details |	Account is created and user is logged in or redirected to login	| ✅ Pass |
| As a new user, I want to be warned if my username already exists | Attempt signup with duplicate username |	Validation error is displayed and account is not created | NOT YET |	
| As a new user, I want password validation so my account is secure	| Enter weak or mismatched passwords	| Clear validation message is shown and form is rejected | ✅ Pass  |	
| As a user, I want to log in so I can access my profile and posts	| Enter valid login credentials | User is authenticated and redirected to Social Feed | ✅ Pass |	
| As a user, I want to be notified if login details are incorrect |	Enter invalid login credentials| Error message is displayed and login fails	| ✅ Pass  |
| As a logged-in user, I want to create a post so I can share my workouts |	Submit a post with image and details |	Post appears on feed and profile | ✅ Pass  |	
| As a logged-in user, I want optional workout fields so I’m not forced to enter extra data	| Create post without workout/intensity |	Post still submits successfully	| ✅ Pass |
| As a user, I want to delete my own posts so I can manage my content | Click delete on a post I created |	Post is removed from database and UI | ✅ Pass  |
| As a user, I should not be able to delete another user’s post |	Manually enter delete URL for another user | Access is denied (403/404) and post remains | ✅ Pass  |
| As a user, I want to comment on posts to interact with others | 	Add a valid comment	| Comment displays under the correct post	 | ✅ Pass  | 
| As a user, I want to edit my own comments | 	Edit an existing comment | 	Updated comment saves and displays correctly | ✅ Pass  | 
| As a user, I should not edit other users’ comments |	Enter another user’s comment edit URL |	Access denied and comment unchanged	| ✅ Pass  |
| As a user, I want to like posts to show engagement | Click like button |	Heart icon changes and like count increases	| ✅ Pass   |
| As a user, I want to unlike posts  | 	Click liked heart again	| Heart icon reverts and like count decreases	 | ✅ Pass  | 
| As a user, I should not be able to like a post multiple times | Attempt repeated likes | Only one like per user per post is stored	| ✅ Pass  |
| As a user, I want responsive navigation on smaller screens  | 	Use hamburger menu on mobile view  | Navbar collapses and links remain usable  | ✅ Pass  | 	
| As a user, I want images to scale correctly on all devices  |	View feed on mobile screen |	Images remain within container and do not overflow |  ✅ Pass  | 
| As a user, I want to see a helpful 404 page when a page doesn’t exist |	Visit invalid URL |	Custom styled 404 page displays with navigation options | ✅ Pass  | 