const activepage = window.location.pathname;
console.log(window.location)
const navlinks = document.querySelectorAll('.navbar').forEach(link => {

    if(link.href.include('${activepage}')){
        link.classList.add('active')
    }
})