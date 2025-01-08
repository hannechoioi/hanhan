//Slide show
let slider = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let dots = document.querySelectorAll('.slider .dots li');

let lengthItems = items.length - 1;
let active = 0;
next.onclick = function(){
    active = active + 1 <= lengthItems ? active + 1 : 0;
    reloadSlider();
}
prev.onclick = function(){
    active = active - 1 >= 0 ? active - 1 : lengthItems;
    reloadSlider();
}
let refreshInterval = setInterval(()=> {next.click()}, 3000);
function reloadSlider(){
    slider.style.left = -items[active].offsetLeft + 'px';
    // 
    let last_active_dot = document.querySelector('.slider .dots li.active');
    last_active_dot.classList.remove('active');
    dots[active].classList.add('active');
    clearInterval(refreshInterval);
    refreshInterval = setInterval(()=> {next.click()}, 3000);
}

dots.forEach((li, key) => {
    li.addEventListener('click', ()=>{
         active = key;
         reloadSlider();
    })
})
window.onresize = function(event) {
    reloadSlider();
};
//Hàm nhập thông tin góp ý
function gopy() {
    hoten=document.frm.hoten.value;
    sodt=document.frm.sodt.value;
    dc=document.frm.dc.value;


    if(hoten==""){
        alert("Chưa nhập tên ! ! !");
        document.frm.hoten.focus();
        return false;
    }
    else if(sodt==""){
        alert("Chưa nhập số điện thoại ! ! !");
        document.frm.sodt.focus();
        return false;
    }
    else if(isNaN(sodt)||sodt.length!=10||eval(sodt)<0){
        alert("Nhập số sai điện thoại sai! ! !");
        document.frm.sodt.focus();
        return false;
    }
    else if(dc==""){
        alert("Chưa nhập địa chỉ !");
    
        document.frm.dc.focus();
        return false;
    }else{
        alert("Cảm ơn đã để lại thông tin !");
        return true;
    }
    

}