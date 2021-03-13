//listening to the page load event as soon as the user make a general.
window.addEventListener('load', (e) => {
    //This event listener will listen to the page load event and as soon as the page get load it will send a fetch request to server with url(hotproperties/) and add the data inside the html tags in (details.html) page.
    e.preventDefault(); //it will prevent the page reloading
    let url = "/hotproperties/"; //url where we are sending the fetch API request.
  
    let options = {
      //there are the GET method options which will go with the API request.
      method: "GET", //GET method.
      headers: {
        //headers will send the info of the content type and csrf token in the backend.
        'content-Type': "application/json",  //data type will be json.
        'X-CSRFToken': csrftoken  //csrftoken verification.
      }
    };
    var html = ""; //empty html var to store the html elements with data.
    const PropertyContainer = document.getElementById('HotPropertyContainer');  //Accessing the property element to insert the filtered properties in it.
    fetch(url, options) //fetch request.
      .then(Response => Response.json())//here we are converting the data into json format.
      .then(data => {
        // this function will append the data into the html variable and in the end it will append the html into PropertyContainer element.
        if (Object.keys(data).length != 0) {
  
          data.forEach(element => {
            //This for loop will iterate over all the element present in the data and one by one it will apppend them into the html variable.
            html += `<div class="col-md-4 col-sm-6">
            <div class="property_item bottom40">
              <div class="image">
                <img src="${element.Property_Image}" alt="listin" class="img-responsive" style="height: 190px;">
                <div class="property_meta">
                  <span><i class="fa fa-object-group"></i>${element.Project_Area}</span>
                  <span><i class="fa fa-bed"></i>1,2,3</span>
                  <span><i class="fa fa-bath"></i>1|2 Bathroom</span>
                </div>
                <div class="price"><span class="tag">For Sale</span></div>
                <div class="overlay">
                  <div class="centered"><a class="link_arrow white_border" href="/HotProperty/${element.slug}/${element.Location}">View Detail</a></div>
                </div>
              </div>
              <div class="proerty_content">
                <div class="proerty_text">
                  <h4><a href="/HotProperty/${element.slug}/${element.Location}">${element.PropertyName}</a></h4>
                  <span>${element.PropertyAddress}, ${element.Location}</span>
                      <p class="p-font-15" style="text-overflow: ellipsis;overflow: hidden;white-space: nowrap;">${element.Property_Description}</p>
                </div>
                <div class="favroute clearfix">
                  <p class="pull-md-left" data-target="#SiteVisitModal" role="button" data-toggle="modal">Contact for Pricing and Offers</p>
                  <ul class="pull-right">
                    <li><a href="#."><i class="icon-video"></i></a></li>
                    <li><a href="#."><i class="icon-like"></i></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>`;
          });
          PropertyContainer.innerHTML = html; //Appending the data into the PropertyContainer div block.
  
        } else {
          //if the there is no data caming form the backend it will the add the below message into the PropertyContainer.
          html += `<div class="col-xs-12 col-sm-8 col-md-8 property-list-list-info">
                    <div class="col-xs-12 col-sm-6 col-md-6">
                      <h3>No Result's Found!</h3>
                      <br>
                      <h4>Please fill the fields correctly!</h4>
                      </div>
                  </div>`;
          //Accessing the property element to insert the filtered properties in it.
          PropertyContainer.innerHTML = html;  //Appending the data into the PropertyContainer div block.
        }
      })
      .catch(() => {
        //if the some error came form the backend it will the add the below message into the PropertyContainer.
        html += `<div class="col-xs-12 col-sm-8 col-md-8 property-list-list-info">
                  <div class="col-xs-12 col-sm-6 col-md-6">
                    <h3>Server Error!Please Try After Some Time.</h3>
                  </div>
                </div>`;
        //Accessing the property element to insert the filtered properties in it.
        PropertyContainer.innerHTML = html;  //Appending the data into the PropertyContainer.
      });
  });
  