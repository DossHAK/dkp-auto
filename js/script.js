const form = document.getElementById('form');

form.addEventListener('submit', getFormValue);

function getFormValue(event) {
    event.preventDefault();
    
    const date = form.querySelector('[id="date"]'),
    city = form.querySelector('[id="city"]'),
    fio_pro = form.querySelector('[id="fio_pro"]'),
    date_birth_pro = form.querySelector('[id="date_birth_pro"]'),
    pasport_pro_s = form.querySelector('[id="pasport_pro_s"]'),
    pasport_pro_n = form.querySelector('[id="pasport_pro_n"]'),
    pasport_pro_kod = form.querySelector('[id="pasport_pro_kod"]'),
    pasport_pro_date = form.querySelector('[id="pasport_pro_date"]');

    const data = {
        date: date.value,
        city: city.value,
        fio_pro: fio_pro.value,
        date_birth_pro: date_birth_pro.value
}};

console.log(data);
