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

| Signup (valid) |	Create a new account with valid username/password (and email if used) | Account created successfully and user is logged in / redirected		| ✅ Works | ![screenshot]() |
| Signup (duplicate username)	| Attempt to sign up using an existing username	| Form displays error and prevents account creation		| ✅ Works | ![screenshot]() |
| Signup (password mismatch) |	Enter two different passwords in password fields |	Validation error shown and account not created	| ✅ Works | ![screenshot]() |	
| Signup (weak password)	| Enter a password | | ✅ Works | ![screenshot]()  |	