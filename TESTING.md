
## Manual tests:



### __Welcome Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Welcome screen has loaded correctly and as intended | Pass |
| Verified that the user can click sign-up button when not authenticated | Pass |
| Verified that the user can click login button when not authenticated | Pass |
| Verified that the user can click brows recipes button when authenticated | Pass |
| Verified that the user can click your recipes button when authenticated | Pass |
| Verified that the user can search recipe when authenticated | Pass |
| Verified that the user can scroll carousell pictures | Pass |
| Verified that the user can click each of footer links and all open on a new page | Pass |
| Verified that the user can click links in navbar and each link opens as intended | Pass |
| Verified that the user can click recipe link when authenticated | Pass |
| Verified that the user can click category link when authenticated | Pass |
| Verified that the user can click blog link when authenticated | Pass |
| Verified that the user can click user link when authenticated | Pass |
| Verified that the user can use a drop down link when authenticated | Pass |
| Verified that the user can choose user profile from user dropdown when authenticated | Pass |
| Verified that the user can choose user my recipe from user dropdown when authenticated | Pass |
| Verified that the user can choose user add recipe from user dropdown when authenticated | Pass |
| Verified that the user can logout from user profile dropdown when authenticated | Pass |
| Verified that the superuser can add category from user dropdown when authenticated | Pass |
| Verified that the superuser can go to django admin site from user dropdown when authenticated | Pass |
</details>

### __Recipes Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Welcome screen has loaded correctly and as intended | Pass |
| Verified that the user can open recipes loaded when authenticated | Pass |
| Verified that the user can open author profile by clicking its name | Pass |
| Verified that the user can open category page by clicking category name | Pass |
| Verified that pagination is working as intended | Pass |
</details>

### __Recipe Details Screen__ (after clicking recipe title)

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Recipes screen has loaded correctly and as intended  | Pass |
| Verified that the user can like or unlike recipe when authenticated | Pass |
| Verified that when the user likes/ulikes recipe a relevant message pops up  | Pass |
| Verified that the user can write a comment when authenticated | Pass |
| Verified that when the user writes a comment a relevant message pops up  | Pass |
| Verified that the back to blog & back to recipes buttons work as intended | Pass |
</details>

### __Category Screen__ 

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Category screen has loaded correctly and as intended | Pass |
| Verified that the categories load randomly each time page is reloaded | Pass |
| Verified that the user can click category name to open a list of recipes in chosen category | Pass |
| Verified that the list of categoriesed recipes is loading correctly | Pass |
| Verified that if the category does not contain any recipes, correct message and buttons are shown  | Pass |
| Verified that when no recipes to be displayed in category view  add recipe buttons is shown  | Pass |
| Verified that the back to category & back to recipes buttons work as intended | Pass |
</details>

### __Blog Screen__ 

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Blog screen has loaded correctly and as intended | Pass |
| Verified that the User can open Recipe view by clicking its title | Pass |
| Verified that the User can open Author profile page by clicking 'Author' tag | Pass |
| Verified that the User can open Category page by clicking 'Category' tag | Pass |
| Verified that the User can continue reading blog by clicking 'CONTINUE READING' link | Pass |
| Verified that pagination is working as intended | Pass |
</details>

### __Blog Details Screen__ (after clicking blog title)

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Blog Detail screen has loaded correctly and as intended | Pass |
| Verified that Users comments are display correctly | Pass |
| Verified that the User pic/deatails display correctly | Pass |
| Verified that the User can like or unlike Recipe Post as intended | Pass |
| Verified that the User gets message that the after like/inlike is shown correctly | Pass |
| Verified that the User can comment Recipe Post as intended | Pass |
| Verified that the User gets message that the comment has been added and awaits Admin's verfication| Pass |
| Verified that the Superuser can delete comment from the list of comments as intended | Pass |
| Verified that the back to blog & back to recipes buttons work as intended | Pass |
</details>

### __Profile Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| My Profile screen has loaded correctly and as intended | Pass |
| Verified that 'Edit Bio & Social Links' button brings user to edit page | Pass |
| Verified that 'Edit Profile Settings' button brings user to edit page | Pass |
| Verified that 'Back to Your Recipes' button brings user to my recipes page | Pass |
| Verified that 'Back to Blog' button brings user to blog page | Pass |
| Verified that each social media links opens correctly | Pass |
</details>

### __Edit Bio & Social Links Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Edit Bio & Social Links screen has loaded correctly and as intended | Pass |
| Verified that the User can update Bio | Pass |
| Verified that the User can update Profile pic | Pass |
| Verified that the User can update All Social Links | Pass |
| Verified that 'Back to Your Profile' button brings user to profile page | Pass |
</details>

### __Edit Profile Settings Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Edit Profile Settings screen has loaded correctly and as intended | Pass |
|  | Pass |

</details>

### __Add Recipe Screen__ 

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Add Recipe screen has loaded correctly and as intended | Pass |
| Verified that the User is presented with a form to be completed as intended | Pass |
| Verified that the 'Recipe' Title field is mandatory | Pass |
| Verified that the 'Category' field is mandatory | Pass |
| Verified that the 'Category' field is pulls data from Category model as intended | Pass |
| Verified that the 'Feature Comment' field is mandatory | Pass |
| Verified that the 'Recipe ingridients' & 'Recipe instructions' fields are shown as Summernote fields | Pass |
| Verified that the User can add additionl information in Excerpt field (not mandatory) | Pass |
| Verified that the User can add image which is saved in Cloudinary | Pass |
| Verified that the User is shown page and message on succesfull submittion | Pass |
| Verified that 'Back' button brings user to recipes page | Pass |
</details>

### __Add Category Screen__ (Superuser only)

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Add Category screen has loaded correctly and as intended | Pass |
| Verified that the Superuser is presented with a form to be completed as intended | Pass |
| Verified that the 'Category Name' field is mandatory | Pass |
| Verified that the 'Category Comment' field is mandatory | Pass |
| Verified that the Superuser can add image which is saved in Cloudinary | Pass |
| Verified that the Superuser is redirected to Category page and is shown a message on succesfull submittion | Pass |
| Verified that 'Back' button brings user to recipes page | Pass |
</details>

### __Admin__ (Superuser only)

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Super user can user a quick link from User manu to open Admin Panel | Pass |
</details>

***

# Browser Compatibility

After publishing to Heroku, the site was tested on Google Chrome, Microsoft Edge, Safari and Mozilla Firefox, with no visible issues for the user. 
The site has loaded correctly and had no issues across all browsers.

# __Validation__

## __HTML__

<details><summary> >>> Click for Recipe validation img</summary>

![Recipe](README/validators/recipe.png)
</details>


<details><summary> >>> Click for Add Recipe validation img</summary>

![Add Recipe](README/validators/add-recipe.png)
</details>


<details><summary> >>> Click for Categories validation img</summary>

![Categories](README/validators/categories.png)
</details>


<details><summary> >>> Click for My Recipes validation img</summary>

![My Recipes](README/validators/my-recipes.png)
</details>


<details><summary> >>> Click for Profile Edit validation img</summary>

![Profile Edit](README/validators/profile-edit.png)
</details>



<details><summary> >>> Click XXX validation img</summary>
</details>

[Back to top &uarr;](#validation)
***
## __CSS__
<details><summary> >>> Click for CSS validation img</summary>

![CSS Validator 1](README/validators/w3ccss.png)
![CSS Validator 2](README/validators/w3ccss-warnings.png)
</details>

[Back to top &uarr;](#validation)
***
## __JS__
<details><summary> >>> Click for JSHint validation img</summary>


</details>

[Back to top &uarr;](#validation)
***
## __Lighthouse__

<details><summary> >>> Click for Home Page Lighthouse Report</summary>
Desktop 

![Home](README/lighthouse/home.png)

Mobile


</details>

***

<details><summary> >>> Click for Recipe Page Lighthouse Report</summary>
Desktop 

![Recipe](README/lighthouse/recipe-desktop.png)

Mobile

![Recipe](README/lighthouse/recipe-mobile.png)
![Recipe details](README/lighthouse/recipe-mobile-pref.png)
</details>

***

<details><summary> >>> Click for Recipe Details Page Lighthouse Report</summary>
Desktop 



Mobile


</details>

***

<details><summary> >>> Click for Category Page Lighthouse Report</summary>
Desktop 

![Category](README/lighthouse/categories-desktop.png)

Mobile

![Category](README/lighthouse/categories-mobile.png)
</details>

***

<details><summary> >>> Click for Category List Page Lighthouse Report</summary>
Desktop 



Mobile


</details>

***

<details><summary> >>> Click for Blog Page Lighthouse Report</summary>
Desktop 

![Blog](README/lighthouse/blog-desktop.png)

Mobile

![Blog](README/lighthouse/blog-mobile.png)
</details>

***

<details><summary> >>> Click for Blog Details Lighthouse Report</summary>
Desktop 



Mobile


</details>

***

<details><summary> >>> Click for Profile Page Lighthouse Report</summary>
Desktop 

![Profile](README/lighthouse/profile-desktop.png)

Mobile

![Profile](README/lighthouse/profile-mobile.png)

</details>

***

<details><summary> >>> Click for Profile Bio Page Lighthouse Report</summary>
Desktop 

![Profile Bio](README/lighthouse/profile-bio-desktop.png)

Mobile

![Profile Bio](README/lighthouse/profile-bio-mobile.png)
</details>

***


<details><summary> >>> Click for Profile Edit Page Lighthouse Report</summary>
Desktop 

![Profile Edit](README/lighthouse/profile-edit-desktop.png)

Mobile

![Profile Edit](README/lighthouse/profile-edit-mobile.png)
</details>

***

<details><summary> >>> Click for Login Page Lighthouse Report</summary>
Desktop 

![Login](README/lighthouse/login-desktop.png)

Mobile

![Login](README/lighthouse/login-mobile.png)
</details>

***






## __PEP8 CI Validation__

***
app: __shemmylicious__

<details><summary> >>> Click for urls.py validation img</summary>

![urls](README/pep8/shemmylicious/urls.png)
</details>

[Back to top &uarr;](#validation)
***
app: __members__

<details><summary> >>> Click for urls.py validation img</summary>

![urls](README/pep8/members/urls.png)
</details>

<details><summary> >>> Click for views.py validation img</summary>

![views](README/pep8/members/views.png)
</details>

<details><summary> >>> Click for forms.py validation img</summary>

![Forms](README/pep8/members/forms.png)
</details>

[Back to top &uarr;](#validation)
***
app: __blog__

<details><summary> >>> Click for urls.py validation img</summary>

![urls](README/pep8/blog/urls.png)
</details>

<details><summary> >>> Click for views.py validation img</summary>

![views](README/pep8/blog/views.png)
</details>

<details><summary> >>> Click for forms.py validation img</summary>

![forms](README/pep8/blog/forms.png)
</details>

<details><summary> >>> Click for models.py validation img</summary>

![models](README/pep8/blog/models.png)
</details>

<details><summary> >>> Click for admin.py validation img</summary>

![admin](README/pep8/blog/admin.png)
</details>

[Back to top &uarr;](#validation)
***



    - [Manual tests](#manual-tests)
    - 
    - [Bugs](#bugs)
    - [Browser Compatibility](#browser-compatibility)


   
## Tests based on user stories


|     |                                   Story                     | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| 1   |        | Yes             |


***


### __Bugs:__
#### __get_lines function__


***

#### __Known Bugs__


GSAP Warnings



***
Back to [README.md](README.md) file.