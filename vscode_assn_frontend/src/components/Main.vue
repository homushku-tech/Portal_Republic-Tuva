<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        items: []
      };
    },
    created() {
      this.fetchData();
    },
    methods: {
      async fetchData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/orders/');
          this.items = response.data;
        } catch (error) {
          console.error(error);
        }
      }
    }
  };
</script>

<template>
    <div class="Jumbotron"  v-for="item in items" :key="item.id">
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
                   {{item.name }}
                </h4>
            </a>
        </div>
        <div class="image_news">
        </div>
        <div class="description_news">
            <p>{{ item.text }}</p>
        </div>

    </div>
</template>

<style>
.header_news {
    display: flex;
    flex-direction: row;
}

.header_news .header_news_tag {
    padding-left: 1vh;
}
</style>
