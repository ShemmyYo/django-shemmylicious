
## Manual tests:



### __Welcome Screen__

<details><summary> >>> Click for details</summary>

- Welcome screen has loaded correctly and as intended.
- Verified that the user can click sign-up button when not authenticated
- Verified that the user can click login button when not authenticated
- Verified that the user can click brows recipes button when authenticated
- Verified that the user can click your recipes button when authenticated
- Verified that the user can search recipe when authenticated
- Verified that the user can scroll carousell pictures
- Verified that the user can click each of footer links and all open on a new page
- Verified that the user can click links in navbar and each link opens as intended
- Verified that the user can click recipe link when authenticated
- Verified that the user can click category link when authenticated
- Verified that the user can click blog link when authenticated
- Verified that the user can click user link when authenticated
- Verified that the user can use a drop down link when authenticated
- Verified that the user can choose user profile from user dropdown when authenticated
- Verified that the user can choose user my recipe from user dropdown when authenticated
- Verified that the user can choose user add recipe from user dropdown when authenticated
- Verified that the user can logout from user profile dropdown when authenticated
- Verified that the superuser can add category from user dropdown when authenticated
- Verified that the superuser can go to django admin site from user dropdown when authenticated
</details>

### __Recipes Screen__

<details><summary> >>> Click for details</summary>

- Welcome screen has loaded correctly and as intended.
- Verified that the user can open recipes loaded when authenticated
- Verified that the user can open author profile by clicking its name
- Verified that the user can open category page by clicking category name
- Verified that pagination is working as intended
</details>

### __Recipe Details Screen__ (after clicking recipe title)

<details><summary> >>> Click for details</summary>

- Recipes screen has loaded correctly and as intended.
- Verified that the user can like or unlike recipe when authenticated
- Verified that when the user likes/ulikes recipe a relevant message pops up 
- Verified that the user can write a comment when authenticated
- Verified that when the user writes a comment a relevant message pops up 
- Verified that the back to blog & back to recipes buttons work as intended
</details>

### __Category Screen__ (after clicking recipe title)

<details><summary> >>> Click for details</summary>

- Category screen has loaded correctly and as intended.
- Verified that the categories load randomly each time page is reloaded
- Verified that the user can click category name to open a list of recipes in chosen category
- Verified that the list of categoriesed recipes is loading correctly
- Verified that if the category does not contain any recipes, correct message and buttons are shown 
- Verified that when no recipes to be displayed in category view  add recipe buttons is shown 
- Verified that the back to category & back to recipes buttons work as intended
</details>

### __Blog Screen__ (after clicking recipe title)

<details><summary> >>> Click for details</summary>

- Category screen has loaded correctly and as intended.
- Verified that the categories load randomly each time page is reloaded
- Verified that the user can click category name to open a list of recipes in chosen category
- Verified that the list of categoriesed recipes is loading correctly
- Verified that if the category does not contain any recipes, correct message and buttons are shown 
- Verified that when no recipes to be displayed in category view  add recipe buttons is shown 
- Verified that the back to category & back to recipes buttons work as intended
</details>

---


***




# Browser Compatibility

After publishing to Heroku, the site was tested on Google Chrome, Microsoft Edge, Safari and Mozilla Firefox, with no visible issues for the user. 
The site has loaded perfectly and had no issues across all browsers.

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

<details><summary> >>> Click for Category Page Lighthouse Report</summary>
Desktop 

![Category](README/lighthouse/categories-desktop.png)

Mobile

![Category](README/lighthouse/categories-mobile.png)
</details>

***

<details><summary> >>> Click for Blog Page Lighthouse Report</summary>
Desktop 

![Blog](README/lighthouse/blog-desktop.png)

Mobile

![Blog](README/lighthouse/blog-mobile.png)
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





***
Back to [README.md](README.md) file.