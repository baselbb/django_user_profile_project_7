# Django User Profile
## Notes
This project utilizes third-party plugins:
* [TinyMCE](https://www.tinymce.com/) javascript enhanced editor for editing the profile bio
* [PWStrength](http://matoilic.github.com/jquery.pwstrength) to display a password strength meter when creating a new password after signup
  
## Project Requirements Summary

**Build a form that takes in details about a registered user and displays those details on a profile page.**
* The profile page should only be visible once the user has logged in.
* The profile page should include first name, last name, email, date of birth, confirm email, short bio and the option to upload an avatar.
* You’ll also set up validation for email, date of birth and the biography. 
* The Date of Birth validation should accept three date formats: YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY. 
* The Email validation should check if the email addresses match and are in a valid format. 
* The bio validation should check that the bio is 10 characters or longer and properly escapes HTML formatting.
* Create a "change password page" that updates the user’s password. 
* This page will ask for current password, new password and confirm password. 
* Set up validation which checks that the current password is valid, that the new password and confirm password fields match
  * New password follows the following policy:
  * must not be the same as the current password
  * minimum password length of 14 characters.
  * must use of both uppercase and lowercase letters
  * must include of one or more numerical digits
  * must include of special characters, such as @, #, $
  * cannot contain the username or parts of the user’s full name, such as his first name
