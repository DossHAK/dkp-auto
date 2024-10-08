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
    pasport_pro_date = form.querySelector('[id="pasport_pro_date"]'),
    
    fio_po = form.querySelector('[id="fio_po"]'),
    date_birth_po = form.querySelector('[id="date_birth_po"]'),
    pasport_po_s = form.querySelector('[id="pasport_po_s"]'),
    pasport_po_n = form.querySelector('[id="pasport_po_n"]'),
    pasport_po_kod = form.querySelector('[id="pasport_po_kod"]'),
    pasport_po_reg = form.querySelector('[id="pasport_po_reg"]'),
    
    model = form.querySelector('[id="model"]'),
    vin = form.querySelector('[id="vin"]'),
    type = form.querySelector('[id="type"]'),
    year = form.querySelector('[id="year"]'),
    engine_m = form.querySelector('[id="engine_m"]'),
    engine_n = form.querySelector('[id="engine_n"]'),
    frame = form.querySelector('[id="frame"]'),
    body = form.querySelector('[id="body"]'),
    km = form.querySelector('[id="km"]'),
    color = form.querySelector('[id="color"]'),

    pts_s = form.querySelector('[id="pts_s"]'),
    pts_n = form.querySelector('[id="pts_n"]'),
    pts_date = form.querySelector('[id="pts_date"]'),
    pts_reg = form.querySelector('[id="pts_reg"]'),
    
    sts_s = form.querySelector('[id="pts_s"]'),
    sts_n = form.querySelector('[id="sts_n"]'),
    sts_date = form.querySelector('[id="sts_date"]'),
    sts_reg = form.querySelector('[id="sts_reg"]'),
    
    number = form.querySelector('[id="number"]'),
    price = form.querySelector('[id="price"]');


    const data = {
        date: date.value,
        city: city.value,
        fio_pro: fio_pro.value,
        date_birth_pro: date_birth_pro.value
}};

console.log(data);
