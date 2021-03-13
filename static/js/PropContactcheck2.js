//Accessing the elements to validate the form and send to the backend.
const Name2 = document.getElementById('username2');  //Name of the user.
const Email2 = document.getElementById('useremail2');  //Email-id of the user.
const Phone2 = document.getElementById('userphone2');  //Phone number of the user.
const Message2 = document.getElementById('usermessage2');  //Message of the user.
const Propdetail2 = document.getElementById('Propdetail2');  //Property name for which the user is looking when he filled this form.
const Form2 = document.getElementById('PropContactform2');  //form.
const SubmitButton2 = document.getElementById('contactsubmit2');  //submit button.
const csrftoken2 = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.

//Alert boxes for individual input
const Namevalid2 = document.getElementById('isnamevalid2');
const Nameinvalid2 = document.getElementById('isnameinvalid2');
const Emailvalid2 = document.getElementById('isemailvalid2');
const Emailinvalid2 = document.getElementById('isemailinvalid2');
const Phonevalid2 = document.getElementById('isphonevalid2');
const Phoneinvalid2 = document.getElementById('isphoneinvalid2');
const Messagevalid2 = document.getElementById('ismessagevalid2');
const Messageinvalid2 = document.getElementById('ismessageinvalid2');

//Alert elements.
const SuccessAlert2 = document.getElementById('issuccess2'); //SuccessAlertElement.
const FailureAlert2 = document.getElementById('isfailure2'); //FailureAlertElement.

//In the start both the Alerts will be hidden.
SuccessAlert2.style.display = 'none';
FailureAlert2.style.display = 'none';

//The alerts will be hidden in the initial time.
Namevalid2.style.display = 'none';
Nameinvalid2.style.display = 'none';
Emailvalid2.style.display = 'none';
Emailinvalid2.style.display = 'none';
Phonevalid2.style.display = 'none';
Phoneinvalid2.style.display = 'none';
Messagevalid2.style.display = 'none';
Messageinvalid2.style.display = 'none';

//variables for checking(these values set to false when the form validation will get completed these values will get changed).
let validName2 = false;
let validEmail2 = false;
let validPhone2 = false;
let validMessage2 = false;


//function for refreshing the page after 20 seconds.
function Refresh() {
    setTimeout(() => {
        location.reload();
    }, 20000);
}

Name2.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear."

    let NameData = Name2.value; //Value inside the name input box.
    let regex = /^[a-z\sA-z]{3,20}$/;  //regex expression.
    let Test = regex.test(NameData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from namevalid and nameinvalid div.
        Namevalid2.style.display = 'block';
        Nameinvalid2.style.display = 'none';
        validName2 = true; //valid Name variable will se changed to true.
    } else {
        //if the test value will be false then the below class will get added and removed from namevalid and nameinvalid div.
        Nameinvalid2.style.display = 'block';
        Namevalid2.style.display = 'none';
    };
});

Email2.addEventListener('blur', () => {
    //Checking the Email of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let EmailData = Email2.value;  //value inside the email input box.
    let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;  //regex expression.
    let Test = regex.test(EmailData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid2.style.display = 'block';
        Emailinvalid2.style.display = 'none';
        validEmail2 = true;
    } else {
        //if the test value will be false then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid2.style.display = 'none';
        Emailinvalid2.style.display = 'block';
    };
});

Phone2.addEventListener('blur', () => {
    //Checking the phone of the user based on the Regex and if it met the conditionthen the success message will appear or failure message will appear.

    let PhoneData = Phone2.value; //value inside the phone input box.
    let regex = /^[0-9]{10}$/;  //regex expression.
    let Test = regex.test(PhoneData);  //testing
    if (Test) {
        //if the test value will be true then the below class will get added and removed from phonevalid and phoneinvalid div.
        Phonevalid2.style.display = 'block';
        Phoneinvalid2.style.display = 'none';
        validPhone2 = true;
    } else {
        //if the test value will be false then the below class will get added and removed from the phonevalid and phoneinvalid div.
        Phonevalid2.style.display = 'none';
        Phoneinvalid2.style.display = 'block';
    };
});

Message2.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let MessageData = Message2.value;  //value inside the message input box.
    let regex = /[a-zA-Z]/;  //regex expression.
    let Test = regex.test(MessageData);  //testing 
    if (Test) {
        //if the test value will be true then the below class will get added in validmessage and invalidmessage.
        Messagevalid2.style.display = 'block';
        Messageinvalid2.style.display = 'none';
        validMessage2 = true;
    } else {
        //if the test value will be false then the below class will get added in validmessage and invalidmessage.
        Messagevalid2.style.display = 'none';
        Messageinvalid2.style.display = 'block';
    };
});


SubmitButton2.addEventListener('click', (event) => {
    //listen to the click event listener and as soon as user clicks on the submit button this function will get executed.
    event.preventDefault(); //this will prevent the page to reload.

    if (validName2 && validEmail2 && validPhone2 && validMessage2) {
        //if all the conditions mentioned above will get true then this function will access all the values of the form and store them into a object convert them into json string and send to the backend by using fetch API.

        //Accessing the userdata from the form.
        var UserData = {
            'Name': Name2.value,
            'Email': Email2.value,
            'Phone': Phone2.value,
            'Message': Message2.value,
            'Propdetail': Propdetail2.value,
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
                    SuccessAlert2.style.display = 'block';  //this is used to show the success alert.
                    FailureAlert2.style.display = 'none';    //this is used to hide the failure alert.
                    Refresh(); //it will refresh the page.
                }
                else if (res.success == false) {
                    Form.reset();  //this is used to reset the form.
                    FailureAlert2.style.display = 'block'; //this is used to show the failure alert.
                    SuccessAlert2.style.display = 'none';    //this is used to hide the success alert.
                    Refresh(); //it will refresh the page.
                }
            }).
            //if any error occured it will show in message.
            catch(() => {
                Form.reset();  //this is used to reset the form.
                FailureAlert2.style.display = 'block'; //this is used to show the failure alert.
                SuccessAlert2.style.display = 'none'; //this is used to hide the success alert.
                Refresh(); //it will refresh the page.
            }
            );

    } else {
        //if any of the data values will left empty it will not submit the form and show the error alert to the user.
        Form.reset();  //this is used to reset the form.
        FailureAlert2.style.display = 'block'; //this is used to show the failure alert.
        SuccessAlert2.style.display = 'none'; //this is used to hide the success alert.
        Refresh(); //it will refresh the page.
    };
});