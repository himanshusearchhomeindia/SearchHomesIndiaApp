//Accessing the elements to validate the form and send to the backend.
const Name3 = document.getElementById('username3');  //Name of the user.
const Email3 = document.getElementById('useremail3');  //Email-id of the user.
const Phone3 = document.getElementById('userphone3');  //Phone number of the user.
const Message3 = document.getElementById('usermessage3');  //Message of the user.
const Propdetail3 = document.getElementById('Propdetail3');  //Property name for which the user is looking when he filled this form.
const Form3 = document.getElementById('PropContactform3');  //form.
const SubmitButton3 = document.getElementById('contactsubmit3');  //submit button.
const csrftoken3 = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.

//Alert boxes for individual input
const Namevalid3 = document.getElementById('isnamevalid3');
const Nameinvalid3 = document.getElementById('isnameinvalid3');
const Emailvalid3 = document.getElementById('isemailvalid3');
const Emailinvalid3 = document.getElementById('isemailinvalid3');
const Phonevalid3 = document.getElementById('isphonevalid3');
const Phoneinvalid3 = document.getElementById('isphoneinvalid3');
const Messagevalid3 = document.getElementById('ismessagevalid3');
const Messageinvalid3 = document.getElementById('ismessageinvalid3');

//Alert elements.
const SuccessAlert3 = document.getElementById('issuccess3'); //SuccessAlertElement.
const FailureAlert3 = document.getElementById('isfailure3'); //FailureAlertElement.

//In the start both the Alerts will be hidden.
SuccessAlert3.style.display = 'none';
FailureAlert3.style.display = 'none';

//The alerts will be hidden in the initial time.
Namevalid3.style.display = 'none';
Nameinvalid3.style.display = 'none';
Emailvalid3.style.display = 'none';
Emailinvalid3.style.display = 'none';
Phonevalid3.style.display = 'none';
Phoneinvalid3.style.display = 'none';
Messagevalid3.style.display = 'none';
Messageinvalid3.style.display = 'none';

//variables for checking(these values set to false when the form validation will get completed these values will get changed).
let validName3 = false;
let validEmail3 = false;
let validPhone3 = false;
let validMessage3 = false;


//function for refreshing the page after 20 seconds.
function Refresh() {
    setTimeout(() => {
        location.reload();
    }, 20000);
}

Name3.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear."

    let NameData = Name3.value; //Value inside the name input box.
    let regex = /^[a-z\sA-z]{3,20}$/;  //regex expression.
    let Test = regex.test(NameData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from namevalid and nameinvalid div.
        Namevalid3.style.display = 'block';
        Nameinvalid3.style.display = 'none';
        validName3 = true; //valid Name variable will se changed to true.
    } else {
        //if the test value will be false then the below class will get added and removed from namevalid and nameinvalid div.
        Nameinvalid3.style.display = 'block';
        Namevalid3.style.display = 'none';
    };
});

Email3.addEventListener('blur', () => {
    //Checking the Email of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let EmailData = Email3.value;  //value inside the email input box.
    let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;  //regex expression.
    let Test = regex.test(EmailData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid3.style.display = 'block';
        Emailinvalid3.style.display = 'none';
        validEmail3 = true;
    } else {
        //if the test value will be false then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid3.style.display = 'none';
        Emailinvalid3.style.display = 'block';
    };
});

Phone3.addEventListener('blur', () => {
    //Checking the phone of the user based on the Regex and if it met the conditionthen the success message will appear or failure message will appear.

    let PhoneData = Phone3.value; //value inside the phone input box.
    let regex = /^[0-9]{10}$/;  //regex expression.
    let Test = regex.test(PhoneData);  //testing
    if (Test) {
        //if the test value will be true then the below class will get added and removed from phonevalid and phoneinvalid div.
        Phonevalid3.style.display = 'block';
        Phoneinvalid3.style.display = 'none';
        validPhone3 = true;
    } else {
        //if the test value will be false then the below class will get added and removed from the phonevalid and phoneinvalid div.
        Phonevalid3.style.display = 'none';
        Phoneinvalid3.style.display = 'block';
    };
})

Message3.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let MessageData = Message3.value;  //value inside the message input box.
    let regex = /[a-zA-Z]/;  //regex expression.
    let Test = regex.test(MessageData);  //testing 
    if (Test) {
        //if the test value will be true then the below class will get added in validmessage and invalidmessage.
        Messagevalid3.style.display = 'block';
        Messageinvalid3.style.display = 'none';
        validMessage3 = true;
    } else {
        //if the test value will be false then the below class will get added in validmessage and invalidmessage.
        Messagevalid3.style.display = 'none';
        Messageinvalid3.style.display = 'block';
    };
});


SubmitButton3.addEventListener('click', (event) => {
    //listen to the click event listener and as soon as user clicks on the submit button this function will get executed.
    event.preventDefault(); //this will prevent the page to reload.

    if (validName3 && validEmail3 && validPhone3 && validMessage3) {
        //if all the conditions mentioned above will get true then this function will access all the values of the form and store them into a object convert them into json string and send to the backend by using fetch API.

        //Accessing the userdata from the form.
        var UserData = {
            'Name': Name3.value,
            'Email': Email3.value,
            'Phone': Phone3.value,
            'Message': Message3.value,
            'Propdetail': Propdetail3.value,
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
                'X-CSRFToken': csrftoken3
            }
        };
        //making the fetch API request.
        fetch('/propertycontactdata/', options). //sending the request to the 'get-response/' end point of the backend.
            then(res => res.json()). //converting the the response into json format.
            then((res) => {
                if (res.success == true) {
                    Form3.reset();  //this is used to reset the form.
                    SuccessAlert3.style.display = 'block';  //this is used to show the success alert.
                    FailureAlert3.style.display = 'none';    //this is used to hide the failure alert.
                    Refresh(); //it will refresh the page.
                }
                else if (res.success == false) {
                    Form3.reset();  //this is used to reset the form.
                    FailureAlert3.style.display = 'block'; //this is used to show the failure alert.
                    SuccessAlert3.style.display = 'none';    //this is used to hide the success alert.
                    Refresh(); //it will refresh the page.
                }
            }).
            //if any error occured it will show in message.
            catch(() => {
                Form3.reset();  //this is used to reset the form.
                FailureAlert3.style.display = 'block'; //this is used to show the failure alert.
                SuccessAlert3.style.display = 'none'; //this is used to hide the success alert.
                Refresh(); //it will refresh the page.
            }
            );

    } else {
        //if any of the data values will left empty it will not submit the form and show the error alert to the user.
        Form3.reset();  //this is used to reset the form.
        FailureAlert3.style.display = 'block'; //this is used to show the failure alert.
        SuccessAlert3.style.display = 'none'; //this is used to hide the success alert.
        Refresh(); //it will refresh the page.
    };
});