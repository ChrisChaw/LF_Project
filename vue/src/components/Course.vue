<template>
  <div class="con">
    <h3>课程列表</h3>
    <div v-for="item in course_data.data">
      <p>{{item.name}}</p>
      <p v-for="obj in item.degreecourse_price_policy">
        <span>{{obj.id}} {{obj.period}} {{obj.price}}</span>
        <button :cid="item.id" :pid="obj.id" v-on:click="add($event)" :price="obj.price" :period="obj._period">添加到购物车</button>
      </p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'course',
    data: function () {
      return {
        course_data: '',
      }
    },
    // 当页面加载完成之后就执行的语句
    mounted() {
      this.get_data();
    },
    methods: {
      get_data: function () {
        var _this = this;
        this.$axios.get('http://127.0.0.1:8001/api/v1/degreecourse/')
          .then(function (response) {
            console.log(response);
            _this.course_data = response.data;
          })
          .catch(function (error) {
            console.log(error);
          });
      },
      add: function (e) {
        var cid = e.target.getAttribute('cid');
        var pid = e.target.getAttribute('pid');
        var period = e.target.getAttribute('period');
        var price = e.target.getAttribute('price');
        this.$axios({
          method: 'post',
          url: 'http://127.0.0.1:8001/api/v1/degreecourse/',
          data: {
            cid: cid,
            pid: pid,
            _period: period,
            price: price,
          }
        });
      }
    },
  }
</script>


<style scoped>

</style>
