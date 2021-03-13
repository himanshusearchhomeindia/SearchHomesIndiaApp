
//Accessing the elements to validate the form and send to the backend.
const Name = document.getElementById('username');  //Name of the user.
const Email = document.getElementById('useremail');  //Email-id of the user.
const Phone = document.getElementById('userphone');  //Phone number of the user.
const Message = document.getElementById('usermessage');  //Message of the user.
const Propdetail = document.getElementById('Propdetail');  //Property name for which the user is looking when he filled this form.
const Form = document.getElementById('PropContactform');  //form.
const SubmitButton = document.getElementById('contactsubmit');  //submit button.
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.

//Alert boxes for individual input
const Namevalid = document.getElementById('isnamevalid');
const Nameinvalid = document.getElementById('isnameinvalid');
const Emailvalid = document.getElementById('isemailvalid');
const Emailinvalid = document.getElementById('isemailinvalid');
const Phonevalid = document.getElementById('isphonevalid');
const Phoneinvalid = document.getElementById('isphoneinvalid');
const Messagevalid = document.getElementById('ismessagevalid');
const Messageinvalid = document.getElementById('ismessageinvalid');

//Alert elements.
const SuccessAlert = document.getElementById('issuccess'); //SuccessAlertElement.
const FailureAlert = document.getElementById('isfailure'); //FailureAlertElement.

//In the start both the Alerts will be hidden.
SuccessAlert.style.display = 'none';
FailureAlert.style.display = 'none';

//The alerts will be hidden in the initial time.
Namevalid.style.display = 'none';
Nameinvalid.style.display = 'none';
Emailvalid.style.display = 'none';
Emailinvalid.style.display = 'none';
Phonevalid.style.display = 'none';
Phoneinvalid.style.display = 'none';
Messagevalid.style.display = 'none';
Messageinvalid.style.display = 'none';

//variables for checking(these values set to false when the form validation will get completed these values will get changed).
let validName = false;
let validEmail = false;
let validPhone = false;
let validMessage = false;


//function for refreshing the page after 20 seconds.
function Refresh() {
    setTimeout(() => {
        location.reload();
    }, 20000);
}

Name.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear."

    let NameData = Name.value; //Value inside the name input box.
    let regex = /^[a-z\sA-z]{3,20}$/;  //regex expression.
    let Test = regex.test(NameData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from namevalid and nameinvalid div.
        Namevalid.style.display = 'block';
        Nameinvalid.style.display = 'none';
        validName = true; //valid Name variable will se changed to true.
    } else {
        //if the test value will be false then the below class will get added and removed from namevalid and nameinvalid div.
        Nameinvalid.style.display = 'block';
        Namevalid.style.display = 'none';
    };
});

Email.addEventListener('blur', () => {
    //Checking the Email of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let EmailData = Email.value;  //value inside the email input box.
    let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;  //regex expression.
    let Test = regex.test(EmailData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid.style.display = 'block';
        Emailinvalid.style.display = 'none';
        validEmail = true;
    } else {
        //if the test value will be false then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid.style.display = 'none';
        Emailinvalid.style.display = 'block';
    };
});

Phone.addEventListener('blur', () => {
    //Checking the phone of the user based on the Regex and if it met the conditionthen the success message will appear or failure message will appear.

    let PhoneData = Phone.value; //value inside the phone input box.
    let regex = /^[0-9]{10}$/;  //regex expression.
    let Test = regex.test(PhoneData);  //testing
    if (Test) {
        //if the test value will be true then the below class will get added and removed from phonevalid and phoneinvalid div.
        Phonevalid.style.display = 'block';
        Phoneinvalid.style.display = 'none';
        validPhone = true;
    } else {
        //if the test value will be false then the below class will get added and removed from the phonevalid and phoneinvalid div.
        Phonevalid.style.display = 'none';
        Phoneinvalid.style.display = 'block';
    };
});

Message.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let MessageData = Message.value;  //value inside the message input box.
    let regex = /[a-zA-Z]/;  //regex expression.
    let Test = regex.test(MessageData);  //testing 
    if (Test) {
        //if the test value will be true then the below class will get added in validmessage and invalidmessage.
        Messagevalid.style.display = 'block';
        Messageinvalid.style.display = 'none';
        validMessage = true;
    } else {
        //if the test value will be false then the below class will get added in validmessage and invalidmessage.
        Messagevalid.style.display = 'none';
        Messageinvalid.style.display = 'block';
    };
});


SubmitButton.addEventListener('click', (event) => {
    //listen to the click event listener and as soon as user clicks on the submit button this function will get executed.
    event.preventDefault(); //this will prevent the page to reload.

    if (validName && validEmail && validPhone && validMessage) {
        //if all the conditions mentioned above will get true then this function will access all the values of the form and store them into a object convert them into json string and send to the backend by using fetch API.

        //Accessing the user data from the form.
        var UserData = {
            'Name': Name.value,
            'Email': Email.value,
            'Phone': Phone.value,
            'Message': Message.value,
            'Propdetail': Propdetail.value,
        };

        //fetch API request.
        //options for sending the fetch API request.
        //1.method
        const options = {
            //there are the POST method options which will go with the API request.
            method: "POST", //POST method.
            body: JSON.stringify(UserData), //User json data.
            headers: {
                //headers will send the info of the content type and csrf token in the backend.
                'content-Type': "application/json",
                'X-CSRFToken': csrftoken
            }
        };
        //making the fetch API request.
        fetch('/propertycontactdata/', options). //sending the request to the 'get-response/' end point of the backend.
            then(res => res.json()). //converting the the response into json format.
            then((res) => {
                if (res.success == true) {
                    Form.reset();  //this is used to reset the form.
                    SuccessAlert.style.display = 'block';  //this is used to show the success alert.
                    FailureAlert.style.display = 'none';    //this is used to hide the failure alert.
                    Refresh(); //it will refresh the page.
                }
                else if (res.success == false) {
                    Form.reset();  //this is used to reset the form.
                    FailureAlert.style.display = 'block'; //this is used to show the failure alert.
                    SuccessAlert.style.display = 'none';    //this is used to hide the success alert.
                    Refresh(); //it will refresh the page.
                }
            }).
            //if any error occured it will show in message.
            catch(() => {
                Form.reset();  //this is used to reset the form.
                FailureAlert.style.display = 'block'; //this is used to show the failure alert.
                SuccessAlert.style.display = 'none'; //this is used to hide the success alert.
                Refresh(); //it will refresh the page.
            }
            );

    } else {
        //if any of the data values will left empty it will not submit the form and show the error alert to the user.
        Form.reset();  //this is used to reset the form.
        FailureAlert.style.display = 'block'; //this is used to show the failure alert.
        SuccessAlert.style.display = 'none'; //this is used to hide the success alert.
        Refresh(); //it will refresh the page.
    };
});