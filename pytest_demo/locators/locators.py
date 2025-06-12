from selenium.webdriver.common.by import By


class locators:

    def __init__(self,driver):
        self.driver=driver

    #login page class
    username = (By.ID,"Email")
    password = (By.ID, "Password")
    login = (By.XPATH,"//input[@class='button-1 login-button']")
    shoppingcarttext = (By.XPATH, "//div/h1[text()='Shopping cart']")
    errormesssagetext = (By.XPATH,"//div/span[text()='Login was unsuccessful. Please correct the errors and try again.']")

    #Books page class
    book = (By.XPATH, "(//div[@class='header-menu']/ul/li/a[@href='/books'])[1]")
    books_list = (By.XPATH, "//div[@class='item-box']")
    shopping_cart_link = (By.XPATH, "//span[text()='Shopping cart']")
    cart_items_checkboxes = (By.XPATH, "//tr[@class='cart-item-row']/td/input[@type='checkbox']")
    terms_condition = (By.ID, "termsofservice")
    submit_button = (By.XPATH, "//button[@type='submit']")
    addtocart = (By.XPATH, ".//input[@value='Add to cart']")
    booksincartlist = (By.XPATH,"//tr[@class='cart-item-row']/td[3]/a")
    billingsave=(By.XPATH,"//input[@onclick='Billing.save()']")
    shippingsave = (By.XPATH, "//input[@onclick='Shipping.save()']")
    shippingmethodsave = (By.XPATH, "//input[@onclick='ShippingMethod.save()']")
    paymentmethodsave=(By.XPATH, "//input[@onclick='PaymentMethod.save()']")
    paymentinfosave=(By.XPATH, "//input[@onclick='PaymentInfo.save()']")
    confirmorder=(By.XPATH, "//input[@onclick='ConfirmOrder.save()']")
    successmessagetext=(By.XPATH, "//div/strong[text()='Your order has been successfully processed!']")
    ordercompleted=(By.XPATH, "//input[@class='button-2 order-completed-continue-button']")
    logout=(By.XPATH, "//a[text()='Log out']")

    #register page class
    register_link= (By.XPATH,"//a[text()='Register']")
    personal_details = "(//div[@class='form-fields'])[1]"
    male=(By.XPATH,personal_details+"//input[@id='gender-male']")
    firstname=(By.XPATH, "//input[@id='FirstName']")
    lastname=(By.XPATH, "//input[@id='LastName']")
    registrationemail=(By.XPATH, "//input[@id='Email']")
    registrationpassword=(By.XPATH, "//input[@id='Password']")
    registrationconfirmpassword=(By.XPATH, "//input[@id='ConfirmPassword']")
    registrationsubmitbutton=(By.XPATH, "//input[@id='register-button']")
    completedtext=(By.XPATH, "//div[@class='result']")

    #search page class
    search_box = (By.XPATH, "//input[@id='small-searchterms']")
    searchoptionslist=(By.XPATH, "(//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']/li)")
    shoppingcartcheckbox=(By.XPATH,"//tr[@class='cart-item-row']/td/input[@type='checkbox']")

    #update shopping cart page
    clickonitem=(By.XPATH,"//div[@class='product-grid home-page-product-grid']/div[4]//div/input")
    clickonaddtocart=(By.XPATH,"//input[@class='button-1 add-to-cart-button']")
    clickonupdateshoppingcart=(By.XPATH,"//input[@name='updatecart']")
    shoppingcartempty=(By.XPATH,"//div[@class='page-body']/div")

    #Basic login functionality
    login_home_page=(By.XPATH,"//a[text()='Log in']")
    verify_email=(By.XPATH,"//a[text()='user467@gmail.com']")
