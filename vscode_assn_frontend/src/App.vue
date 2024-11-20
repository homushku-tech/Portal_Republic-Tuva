<script>
import Main from './components/Main.vue'
export default {
  components: { Main },
  data() {
    return {

    }
  }
}
</script>

<template>

  <div class="div1">
    <img src="./assets/img/main.png">
    <div class="top_navbar">
      <div class="flex-items">
        <a href="">Главная</a>
      </div>
      <div class="flex-items">
        <a href="">О Республике</a>
      </div>
      <div class="flex-items">
        <a href="">Инвестиционный паспорт</a>
      </div>
      <div class="flex-items">
        <a href="">Интернет-приемная</a>
      </div>
      <div class="flex-items">
        <a href="">Официальные документы</a>
      </div>
      <div class="flex-items">
        <a href="">Контакты</a>
      </div>
    </div>
  </div>
  <div class="content">
    <div class="div2">
      <div class="left-navbar-massiv">
        <div class="left-navbar">
          <a href="">Правительство Тувы</a>
        </div>
        <div class="left-navbar">
          <a href="">Деятельность</a>
        </div>
        <div class="left-navbar">
          <a href="">Поручения</a>
        </div>
        <div class="left-navbar">
          <a href="">Документы</a>
        </div>
        <div class="left-navbar">
          <a href="">Кадровая политика</a>
        </div>
      </div>
      <div class="left-navbar-image">
        <div class=left-navbar-image-items>
          <img src="./assets/img/bus.gov.ru.png">
        </div>
        <br>
        <div class=left-navbar-image-items>
          <img src="./assets/img/roads.png">
        </div>
      </div>
    </div>
    <div class="div3">
      <h1 id="main_h1">Главное</h1>
      <Main />
    </div>
    <div class="div4">

    </div>
  </div>
</template>

<style>
.div1 img {
  width: 100%;
  /* height: 100%; */
}

.div1 {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.top_navbar {
  border: 1px solid #34b4eb;
  width: 100%;
  height: 9vh;
  background-color: #34b4eb;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: space-around;
  align-items: stretch;
  align-content: space-between;
}

.flex-items {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: center;
  align-content: stretch;
}

.flex-items a {
  text-decoration: none;
  color: whitesmoke;
  font-size: 20px;
}

.left-navbar {
  display: flex;
  justify-content: center;
  align-items: center;
}
.content{
  display: flex;
  justify-content: space-between; 
}
.div2 {
  position: relative;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  width: 35vh;
  text-align: center;
  flex-grow:0;
}

.left-navbar-massiv {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 35vh;
  text-align: center;
}

.left-navbar-massiv>div {
  background: #f3f0e8;
  border-bottom: 3px solid #ffcc80;
  padding: 18px;
}

.left-navbar a {
  text-decoration: none;
  font-size: 20px;
}

.left-navbar-image-items img {
 
  width: 35vh;
}

.div3 {
  border: 1px solid red;
  position: relative;
  top: 0;
  width: 75vh;
  flex-grow:1;
}

.div3 #main_h1 {
  font-size: 50px;
  color: #34b4eb;
}

.div4 {
  flex-grow:1;

}
</style>
