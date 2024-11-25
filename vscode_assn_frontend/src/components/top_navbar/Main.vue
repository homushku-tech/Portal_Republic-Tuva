<script>
import axios from 'axios';
export default {

  data() {
    return {
      items: [],
      currentPage: 1,
      itemsPerPage: 5,
    };
  },

  created() {
    this.fetchData();
  },
  // Вычисляемое свойство для пагинации, которая создает массив для вывода опред. количества новостных карточек 
  computed: {
    paginatedItems() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.items.slice(start, start + this.itemsPerPage);
    },
  },

  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/orders/');
        this.items = response.data;
        this.items = this.items.reverse()
      } catch (error) {
        console.error(error);
      }
    },
    // Для пагинации
    onClickHandler(page) {
      console.log(page);
      this.currentPage = page; // Обновляем текущую страницу
    },

  }

};
</script>

<template>
  <h1 id="main_h1">Главное</h1>
  <!-- Новостные карточки -->
  <div class="Jumbotron" v-for="item in paginatedItems" :key="item.id">
    <div class="header_news">
      <div class="header_news_date">
        вчера, 19:46
      </div>
      <div class="header_news_tag">
        Строительство
      </div>
    </div>
    <div class="name_news">
      <a href="#">
        <h4>
          {{ item.name }}
        </h4>
      </a>
    </div>
    <div class="image_news">
    </div>
    <div class="description_news">
      <p>{{ item.text }}</p>
    </div>
  </div>
  <!-- Пагинация -->
  <vue-awesome-paginate :total-items="items.length" :items-per-page="5" :max-pages-shown="1" v-model="currentPage"
    @click="onClickHandler" />
</template>

<style>
.Jumbotron {
  border-radius: 2%;
  background-color: #e6e6fa;
  transition: all 1s;
  padding-left: 1vh;
  padding-top: 1vh;
  padding-bottom: .1px;
  margin-bottom: 1vh;

}
.Jumbotron:hover {
  -webkit-box-shadow: 10px 4px 8px 0px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 10px 4px 8px 0px rgba(34, 60, 80, 0.2);
  box-shadow: 10px 4px 8px 0px rgba(34, 60, 80, 0.2);

}
.header_news {
  display: flex;
  flex-direction: row;
}
.header_news .header_news_tag {
  padding-left: 1vh;
}
#main_h1 {
  font-size: 50px;
  color: #34b4eb;
}
</style>
