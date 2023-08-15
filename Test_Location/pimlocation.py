class Pimlocation:
    #add employee1 details
    firstname_input_box = "firstName"  #NAME
    middlename_input_box = "middleName" #NAME
    lastname_input_box = "lastName" #NAME
    employee_id = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input' #XPATH
    

    #create login details for employee1
    create_login_details = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span" #XPATH
    #insert_image = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button/i" #XPATH
    Username ="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input" 
    password = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input"
    confirm_password = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input"
    status_enabled="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span"
    status_disabled='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
    save_button = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"
    save_css="button.oxd-button:nth-child(3)"

    
    #delete employee details

    #delete employee details

    search ='/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    delete_button="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[11]/div/div[9]/div/button[1]"
    confirm_delete="/html/body/div/div[3]/div/div/div/div[3]/button[2]/i"
    yes_del='#app > div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > div.orangehrm-modal-footer > button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin'