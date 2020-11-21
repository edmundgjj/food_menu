# Digital Food Menu Manager #
By: **Edmund Goh Jun Jie** -- *Code Institute Batch 8* -- 
<br>

## OVERVIEW ##

This is a website for a restaurant to showcase their menu digitally especially in this day and age of contactless menu. 
Restaurant managers can ask customers to scan a QR code that brings them to a mobile-responsive digital menu. 

## Database Planning ##

Product Object (For each menu item)
{
    "id";
    "product_name";
    "product_price";
    "product_desc";
    "category":[];
}

## USER EXPERIENCE ## 

- Each menu item is displayed in a form of a card to make it easy to discern each menu item's name, price and description easily. 
- As an administrator, I can visit the administrator URL via "/" to make adjustments to the menu such as create a new menu item, edit a menu item or delete a menu item. 
- The customer facing URL is "/customer" which hides the functionality to create and edit menu items. 
- Both administrator and customer can search the menu items based the name of the item. 
- To help customers find healthy food option and store recommended option easily, they can do so via the filter in the search page. 
- The emphasis of the menu is for customers to be able to see all the items sold by the store, hence the emphasis of the design is via that of a card for each item. 
- The menu is responsive and displays 3 columns of cards for desktop browsing, 2 columns for medium displays and only 1 column for mobile display. 

## FURTHER IMPROVEMENTS ## 
- The ability to upload menu images 
- The ability to group menu items by category
- The ability to edit store information such as store name and store description and add store logo. 
- The ability to accept ordering directly on the digital menu. 
- Administrator account management where a username and login is required to log into website. 

## TECHNOLOGY USED ## 

- HTML, CSS, JS, Bootstrap 4
- Python, Flask, Jinja 2, MongoDB
- Heroku 

## TESTING ## 
- Manual testing is done on IPhone 11 Pro Max and Macbook Pro 16-Inch to ensure that the menu is displayed correctly. 
- Check that validation works where user is not able to create an item without providing product name, product description and price. 
- Check that the search results work based on the product name and category filters applied. 

## DEPLOYMENT ## 
- Deployment is done via Heroku