let calculate = document.querySelector('.calculate');


calculate.addEventListener('click',function(){
    let length = document.getElementById("length").value;
    let weight = document.getElementById("weight").value;
    let bmi = Number(weight / (length * length / 10000)).toFixed(2);
    document.getElementById("BMI").innerHTML = bmi;
    if(bmi <= 25){
        document.getElementById("info").innerHTML = "WEAK";
    }
    else{
        document.getElementById("info").innerHTML = "FAT";
    }

});