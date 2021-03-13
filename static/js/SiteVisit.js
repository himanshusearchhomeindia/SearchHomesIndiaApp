//Accessing the elements to validate the form and send to the backend.
const Name4 = document.getElementById('username4');  //Name of the user.
const Email4 = document.getElementById('useremail4');  //Email-id of the user.
const Phone4 = document.getElementById('userphone4');  //Phone number of the user.
const Message4 = document.getElementById('usermessage4');  //Message of the user.
const Propdetail4 = document.getElementById('Propdetail4');  //Property name for which the user is looking when he filled this form.
const Form4 = document.getElementById('PropContactform4');  //form.
const SubmitButton4 = document.getElementById('contactsubmit4');  //submit button.
const csrftoken4 = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.

//Alert boxes for individual input
const Namevalid4 = document.getElementById('isnamevalid4');
const Nameinvalid4 = document.getElementById('isnameinvalid4');
const Emailvalid4 = document.getElementById('isemailvalid4');
const Emailinvalid4 = document.getElementById('isemailinvalid4');
const Phonevalid4 = document.getElementById('isphonevalid4');
const Phoneinvalid4 = document.getElementById('isphoneinvalid4');
const Messagevalid4 = document.getElementById('ismessagevalid4');
const Messageinvalid4 = document.getElementById('ismessageinvalid4');

//Alert elements.
const SuccessAlert4 = document.getElementById('issuccess4'); //SuccessAlertElement.
const FailureAlert4 = document.getElementById('isfailure4'); //FailureAlertElement.

//In the start both the Alerts will be hidden.
SuccessAlert4.style.display = 'none';
FailureAlert4.style.display = 'none';

//The alerts will be hidden in the initial time.
Namevalid4.style.display = 'none';
Nameinvalid4.style.display = 'none';
Emailvalid4.style.display = 'none';
Emailinvalid4.style.display = 'none';
Phonevalid4.style.display = 'none';
Phoneinvalid4.style.display = 'none';
Messagevalid4.style.display = 'none';
Messageinvalid4.style.display = 'none';

//variables for checking(these values set to false when the form validation will get completed these values will get changed).
let validName4 = false;
let validEmail4 = false;
let validPhone4 = false;
let validMessage4 = false;


//function for refreshing the page after 40 seconds.
function Refresh() {
    setTimeout(() => {
        location.reload();
    }, 40000);
}

Name4.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear."

    let NameData = Name4.value; //Value inside the name input box.
    let regex = /^[a-z\sA-z]{3,40}$/;  //regex expression.
    let Test = regex.test(NameData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from namevalid and nameinvalid div.
        Namevalid4.style.display = 'block';
        Nameinvalid4.style.display = 'none';
        validName4 = true; //valid Name variable will se changed to true.
    } else {
        //if the test value will be false then the below class will get added and removed from namevalid and nameinvalid div.
        Nameinvalid4.style.display = 'block';
        Namevalid4.style.display = 'none';
    };
});

Email4.addEventListener('blur', () => {
    //Checking the Email of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let EmailData = Email4.value;  //value inside the email input box.
    let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;  //regex expression.
    let Test = regex.test(EmailData);  //testing.
    if (Test) {
        //if the test value will be true then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid4.style.display = 'block';
        Emailinvalid4.style.display = 'none';
        validEmail4 = true;
    } else {
        //if the test value will be false then the below class will get added and removed from emailvalid and emailinvalid div.
        Emailvalid4.style.display = 'none';
        Emailinvalid4.style.display = 'block';
    };
});

Phone4.addEventListener('blur', () => {
    //Checking the phone of the user based on the Regex and if it met the conditionthen the success message will appear or failure message will appear.

    let PhoneData = Phone4.value; //value inside the phone input box.
    let regex = /^[0-9]{10}$/;  //regex expression.
    let Test = regex.test(PhoneData);  //testing
    if (Test) {
        //if the test value will be true then the below class will get added and removed from phonevalid and phoneinvalid div.
        Phonevalid4.style.display = 'block';
        Phoneinvalid4.style.display = 'none';
        validPhone4 = true;
    } else {
        //if the test value will be false then the below class will get added and removed from the phonevalid and phoneinvalid div.
        Phonevalid4.style.display = 'none';
        Phoneinvalid4.style.display = 'block';
    };
});

Message4.addEventListener('blur', () => {
    //Checking the name of the user based on the Regex and if it met the condition then the success message will appear or failure message will appear.

    let MessageData = Message4.value;  //value inside the message input box.
    let regex = /[a-zA-Z]/;  //regex expression.
    let Test = regex.test(MessageData);  //testing 
    if (Test) {
        //if the test value will be true then the below class will get added in validmessage and invalidmessage.
        Messagevalid4.style.display = 'block';
        Messageinvalid4.style.display = 'none';
        validMessage4 = true;
    } else {
        //if the test value will be false then the below class will get added in validmessage and invalidmessage.
        Messagevalid4.style.display = 'none';
        Messageinvalid4.style.display = 'block';
    };
});


SubmitButton4.addEventListener('click', (event) => {
    //listen to the click event listener and as soon as user clicks on the submit button this function will get executed.
    event.preventDefault(); //this will prevent the page to reload.

    if (validName4 && validEmail4 && validPhone4 && validMessage4) {
        //if all the conditions mentioned above will get true then this function will access all the values of the form and store them into a object convert them into json string and send to the backend by using fetch API.

        //Accessing the userdata from the form.
        var UserData = {
            'Name': Name4.value,
            'Email': Email4.value,
            'Phone': Phone4.value,
            'Message': Message4.value,
            'Propdetail': Propdetail4.value,
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
                'X-CSRFToken': csrftoken4
            }
        };
        //making the fetch API request.
        fetch('/propertycontactdata/', options). //sending the request to the 'get-response/' end point of the backend.
            then(res => res.json()). //converting the the response into json format.
            then((res) => {
                if (res.success == true) {
                    Form4.reset();  //this is used to reset the form.
                    SuccessAlert4.style.display = 'block';  //this is used to show the success alert.
                    FailureAlert4.style.display = 'none';    //this is used to hide the failure alert.
                    Refresh(); //it will refresh the page.
                }
                else if (res.success == false) {
                    Form4.reset();  //this is used to reset the form.
                    FailureAlert4.style.display = 'block'; //this is used to show the failure alert.
                    SuccessAlert4.style.display = 'none';    //this is used to hide the success alert.
                    Refresh(); //it will refresh the page.
                }
            }).
            //if any error occured it will show in message.
            catch(() => {
                Form4.reset();  //this is used to reset the form.
                FailureAlert4.style.display = 'block'; //this is used to show the failure alert.
                SuccessAlert4.style.display = 'none'; //this is used to hide the success alert.
                Refresh(); //it will refresh the page.
            }
            );

    } else {
        //if any of the data values will left empty it will not submit the form and show the error alert to the user.
        Form4.reset();  //this is used to reset the form.
        FailureAlert4.style.display = 'block'; //this is used to show the failure alert.
        SuccessAlert4.style.display = 'none'; //this is used to hide the success alert.
        Refresh(); //it will refresh the page.
    };
});