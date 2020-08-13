document.getElementById("most-important").style.background = 'white'

can the logic be: 
if a project's area has
 athelete, then color red for project
elseif connected
else if x 


document.getElementsByClassName("most-important").style.background = 'white'


<script>
$(document).ready(function(){

// jQuery methods go here...

  document.getElementsByClassName("aof").innerHTML = greeting;
});
</script>

.athlete {
    background-color: rgba(229, 0, 0, 0.7)
}
.polished-mirror {
    background-color: rgba(229, 103, 0, 0.7)
}
.connection-and-leadership {
    background-color: rgba(250, 237, 50, 0.7)
}
.expand-professionally {
    background-color: rgba(172, 205, 3, 0.7)
}
.security-and-investment {
    background-color: rgba(55, 156, 0, 0.7)
}
.work-projects {
    background-color: rgba(0, 228, 224, 0.7)
}
.technologist {
    background-color: rgba(0, 31, 228, 0.7)
}
.luxury-and-adventure {
    background-color: rgba(182, 1, 228, 0.7)
}



// $(:ul li:tg(0)") this will select all li elements of ul elements with an index of greater than 0
// $(:ul li:eg(0)") this picks the first of the elements in a list
// $(":contains(Athlete)") this will select all the elements taht contain the text Athlete

// should I say 'if it's the first element in the list, then give it the class "most important"