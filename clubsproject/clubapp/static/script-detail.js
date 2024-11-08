document.addEventListener("DOMContentLoaded", function() { // DOMContentLoaded - это событие, которое запускается, когда HTML документ
    // будет полностью загружен и разобран, без ожидания полной загрузки таблиц стилей, изображений и фреймов.
    const category_elem = document.querySelector('.category');
    const category = category_elem.textContent.trim();
    console.log(category)

    ApplyStyles2(category);
});

function ApplyStyles2(element) {
    const necessary_classes = ['body', 'header-header', 'see-more__modal-window', ];
    console.log(necessary_classes)
    for (let i of necessary_classes) {
        const temp = document.querySelector(`.${i}`);
        console.log(temp)
        if (temp) {
            const new_class = `${i}_${element}`;
            console.log(new_class)
            temp.classList.replace(i, new_class);
        }
    }
}