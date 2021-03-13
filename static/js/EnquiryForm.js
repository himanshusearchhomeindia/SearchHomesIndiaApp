
//Accessing the elements to validate the form and send to the backend.
const Name5 = document.getElementById('username5');  //Name of the user.
const Email5 = document.getElementById('useremail5');  //Email-id of the user.
const Phone5 = document.getElementById('userphone5');  //Phone number of the user.
const Message5 = document.getElementById('usermessage5');  //Message of the user.
const Propdetail5 = document.getElementById('Propdetail5');  //Property name for which the user is looking when he filled this form.
const Form5 = document.getElementById('PropContactform5');  //form.
const SubmitButton5 = document.getElementById('contactsubmit5');  //submit button.
const csrftoken5 = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.

//Alert boxes for individual input
const Namevalid5 = document.getElementById('isnamevalid5');
const Nameinvalid5 = document.getElementById('isnameinvalid5');
const Emailvalid5 = document.getElementById('isemailvalid5');
const Emailinvalid5 = document.getElementById('isemailinvalid5');
const Phonevalid5 = document.getElementById('isphonevalid5');
const Phoneinvalid5 = document.getElementById('isphoneinvalid5');
const Messagevalid5 = document.getElementById('ismessagevalid5');
const Messageinvalid5 = document.getElementById('ismessageinvalid5');

//Alert elements.
const SuccessAlert5 = document.getElementById('issuccess5'); //SuccessAlertElement.
const FailureAlert5 = document.getElementById('isfailure5'); //FailureAlertElement.

//In the start both the Alerts will be hidden.
SuccessAlert5.style.display = 'none';
FailureAlert5.style.display = 'none';

//The alerts will be hidden in the initial time.
Namevalid5.style.display = 'none';
Nameinvalid5.style.display = 'none';
Emailvalid5.style.display = 'none';
Emailinvalid5.style.display = 'none';
Phonevalid5.style.display = 'none';
Phoneinvalid5.style.display = 'none';
Messagevalid5.style.display = 'none';
Messageinvalid5.style.display = 'none';

//variables for checking(these values set to false when the form validation will get completed these values will get changed).
let validName5 = false;
let validEmail5 = false;
let validPhone5 = false;
let validMessage5 = false;


//function for refreshing the page after 50 seconds.
function Refresh() {
    setTimeout(() => {
        location.reload();
    }, 50000);
}

Name5.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear."

    let NameData = Name5.value; //Value inside the name input box.
    let regex = /^[a-z\sA-z]{3,50}$/;  //regex expression.
    let Test = regex.test(NameData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from namevalid and nameinvalid div.
        Namevalid5.style.display = 'block';
        Nameinvalid5.style.display = 'none';
        validName5 = true; //valid Name variable will se changed to true.
    } else {
        //if the test value will be false then the below class will get added and removed from namevalid and nameinvalid div.
        Nameinvalid5.style.display = 'block';
        Namevalid5.style.display = 'none';
    };
});

Email5.addEventListener('blur', () => {
    //Checking the Email of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let EmailData = Email5.value;  //value inside the email input box.
    let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;  //regex expression.
    let Test = regex.test(EmailData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid5.style.display = 'block';
        Emailinvalid5.style.display = 'none';
        validEmail5 = true;
    } else {
        //if the test value will be false then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid5.style.display = 'none';
        Emailinvalid5.style.display = 'block';
    };
});

Phone5.addEventListener('blur', () => {
    //Checking the phone of the user based on the Regex and if it met the conditionthen the success message will appear or failure message will appear.

    let PhoneData = Phone5.value; //value inside the phone input box.
    let regex = /^[0-9]{10}$/;  //regex expression.
    let Test = regex.test(PhoneData);  //testing
    if (Test) {
        //if the test value will be true then the below class will get added and removed from phonevalid and phoneinvalid div.
        Phonevalid5.style.display = 'block';
        Phoneinvalid5.style.display = 'none';
        validPhone5 = true;
    } else {
        //if the test value will be false then the below class will get added and removed from the phonevalid and phoneinvalid div.
        Phonevalid5.style.display = 'none';
        Phoneinvalid5.style.display = 'block';
    };
});

Message5.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let MessageData = Message5.value;  //value inside the message input box.
    let regex = /[a-zA-Z]/;  //regex expression.
    let Test = regex.test(MessageData);  //testing 
    if (Test) {
        //if the test value will be true then the below class will get added in validmessage and invalidmessage.
        Messagevalid5.style.display = 'block';
        Messageinvalid5.style.display = 'none';
        validMessage5 = true;
    } else {
        //if the test value will be false then the below class will get added in validmessage and invalidmessage.
        Messagevalid5.style.display = 'none';
        Messageinvalid5.style.display = 'block';
    };
});


SubmitButton5.addEventListener('click', (event) => {
    //listen to the click event listener and as soon as user clicks on the submit button this function will get executed.
    event.preventDefault(); //this will prevent the page to reload.

    if (validName5 && validEmail5 && validPhone5 && validMessage5) {
        //if all the conditions mentioned above will get true then this function will access all the values of the form and store them into a object convert them into json string and send to the backend by using fetch API.

        //Accessing the userdata from the form.
        var UserData = {
            'Name': Name5.value,
            'Email': Email5.value,
            'Phone': Phone5.value,
            'Message': Message5.value,
            'Propdetail': Propdetail5.value,
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
                'X-CSRFToken': csrftoken5
            }
        };
        //making the fetch API request.
        fetch('/propertycontactdata/', options). //sending the request to the 'get-response/' end point of the backend.
            then(res => res.json()). //converting the the response into json format.
            then((res) => {
                if (res.success == true) {
                    Form5.reset();  //this is used to reset the form.
                    SuccessAlert5.style.display = 'block';  //this is used to show the success alert.
                    FailureAlert5.style.display = 'none';    //this is used to hide the failure alert.
                    Refresh(); //it will refresh the page.
                }
                else if (res.success == false) {
                    Form5.reset();  //this is used to reset the form.
                    FailureAlert5.style.display = 'block'; //this is used to show the failure alert.
                    SuccessAlert5.style.display = 'none';    //this is used to hide the success alert.
                    Refresh(); //it will refresh the page.
                }
            }).
            //if any error occured it will show in message.
            catch(() => {
                Form5.reset();  //this is used to reset the form.
                FailureAlert5.style.display = 'block'; //this is used to show the failure alert.
                SuccessAlert5.style.display = 'none'; //this is used to hide the success alert.
                Refresh(); //it will refresh the page.
            }
            );

    } else {
        //if any of the data values will left empty it will not submit the form and show the error alert to the user.
        Form5.reset();  //this is used to reset the form.
        FailureAlert5.style.display = 'block'; //this is used to show the failure alert.
        SuccessAlert5.style.display = 'none'; //this is used to hide the success alert.
        Refresh(); //it will refresh the page.
    };
});