function MenuAction() {
  let menulist = document.getElementById("popup")
  if (menulist.style.display === "none") {
    menulist.style.display = "block"
  }
  else {
    menulist.style.display = "none"
  }
}

document.addEventListener("DOMContentLoaded", function() { // DOMContentLoaded - это событие, которое запускается, когда HTML документ
    // будет полностью загружен и разобран, без ожидания полной загрузки таблиц стилей, изображений и фреймов.
    all_cont = document.querySelectorAll('.wrapper')
    all_cont_buttons = document.querySelectorAll('.form_categories')
    for (let container of all_cont) {
        const category_elem = container.querySelector('.category');
        const category = category_elem.textContent.trim();
        console.log(category)
        ApplyStyles(category, container);
    }
    for (let button of all_cont_buttons) {
        const button_elem = button.querySelector('.course-button-text');
        const category_button = button_elem.textContent.trim();
        console.log(category_button)
        ApplyStyles(category_button, button);
    }
});

function ApplyStyles(element, container) {
    const necessary_classes = ['badge', 'button', 'badge-desc'];
    console.log(necessary_classes)
    for (let i of necessary_classes) {
        const temp = container.querySelector(`.${i}`);
        console.log(temp)
        if (temp) {
            const new_class = `${i}-${element}`;
            console.log(  new_class)
            temp.classList.replace(i, new_class);
        }
    }
}

function see_moreAction() {
  let menuList = document.getElementById("see-more__modal-window");
  let body = document.getElementById("body_id");
  const category_elem = document.querySelector('.category');
  const category = category_elem.textContent.trim();
  console.log("category_elem", category_elem)
  if (menuList.style.display === "none") {
      menuList.style.display = "flex";
      if (category == 'sport') {
          body.style.boxShadow = "inset 530px 530px #A7A7A7"
      }

  } 
  else {
      menuList.style.display = "none" 
  }
}


function close_ModalWindow() {
  const category_elem = document.querySelector('.category');
  const category = category_elem.textContent.trim();
  let groups_all = document.getElementById('see-more__modal-window');
  let body = document.getElementById("body_id");
  if (groups_all.style.display === "flex") {
      groups_all.style.display = "none"
      if (category == 'sport') {
          body.style.boxShadow = "none"
      }

  }
  else {
      groups_all.style.display = "flex"
  }
}
