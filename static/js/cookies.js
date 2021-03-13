let url = document.location.href;  //storing the url here.

$(document).ready(function () {
    //checking the cookies when the page load's.
    CheckCookie();
  });

//function to get the cookies.
function GetCookie(cname) {
    //This function will take the cookies name as a parameter.
    let name = cname + "="; //create a name dividing the cookies values.
    let decodedCookie = decodeURIComponent(document.cookie);  //decode the cookie string  to handle cookies with special characters.
    let CapturedCookie = decodedCookie.split(';');  //split document.cookie on semicolon into an array.
    for (let i = 0; i < CapturedCookie.length; i++) {
        //loop through the CapturedCookie.
        var Cook = CapturedCookie[i];
        while (Cook.charAt(0) == ' ') {
            Cook = Cook.substring(1);
        }
        if (Cook.indexOf(name) == 0) {
            //if the cookie value is found return the value of the cookie.
            return Cook.substring(name.length, Cook.length)
        }
        else{
        return "";
        }
    }
};

//function for setting the colkies.
function SetCookies(cname, cvalue) {
    var date = new Date();  //get the date library to store the cookies for longer time.
    date.setTime(date.getTime() + 365 * 24 * 60 * 60 * 100);  //this will set the cookie time how long it will be saved in the browser.
    let exp = "Expires" + date.toUTCString();  //converting the time into utc and adding the expire time with it.
    document.cookie = cname + "=" + cvalue + ";" + exp;  // here it will store the cookie into browsers.
};

//function to check the cookie name.
function CheckCookie() {
    let StoredCookies = GetCookie("URLCookies");  //it will check whether there are cookies are stored or not.
    //if the cookies are not there it will show the modal to the user to accept the cookies.
    if (StoredCookies == "") {
        $("#myModal1").modal('show');
            $('#myModal1').modal({
                backdrop: 'static',
                keyboard: false
            });
        //if the cookies are not there it will access the url and store it in cookies.
        let Accept = document.getElementById('Accept');
        Accept.addEventListener('click', ()=>{
            SetCookies("URLCookies", url);
            $("#myModal1").modal('hide');
        });
        //setting the model display sittings to hide.
    }
    else{
        //if there are some cookies present in the stored cookies variable it will set the new values by using the setcookie function.
        SetCookies("URLCookies", StoredCookies);  
        //setting the model display sittings to none.
    }
};
