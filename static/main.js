//pull the pathname from window location
const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});


// calculate age
function birthdayalert() {
    var name = document.getElementById("first_name").value + ' ' +document.getElementById("last_name").value + ', ';
    var birthDate= document.getElementById("date-input").value;
    var dob = new Date(birthDate);  
    var entered_year= dob.getFullYear();     //extracting year from input date
    var entered_month= dob.getMonth();  

    var now =new Date();                            //getting current date
    var currentY= now.getFullYear();                //extracting year from the date
    var currentM= now.getMonth();


    var ageY =currentY - entered_year;

    if (ageY > 0 && currentM - entered_month < 0){
      ageY -=1
    }
    var ageM =Math.abs(currentM- entered_month);

    alert(name + ageY +' years old') // raise alert of current age
}

// show/hide image function
function setImageVisible(id, visible) {
  var img = document.getElementById(id);
  img.style.visibility = (visible ? 'visible' : 'hidden');
}

