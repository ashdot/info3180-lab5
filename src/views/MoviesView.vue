<template>
  <div class="container mt-4">
    <h2 class="mb-2">Movies</h2>

    <div class="row">

      <div
        class="col-md-6 mb-2"
        v-for="movie in movies"
        :key="movie.id"
      >
        <div class="card mb-3">
        <div class="row g-0">

            <!-- Image (left side) -->
            <div class="col-md-4">
            <img :src="movie.poster" class="movie-img img-fluid rounded-start" />
            </div>

            <!-- Text (right side) -->
            <div class="col-md-8">
            <div class="card-body">
                <h5 class="card-title">{{ movie.title }}</h5>
                <p class="card-text">{{ movie.description }}</p>
            </div>
            </div>

        </div>
        </div>
        </div>
      </div>

    </div>

</template>





<script setup>
import { ref, onMounted } from "vue";

const movies = ref([])

function fetchMovies() {

  fetch("/api/v1/movies")
    .then(response => {
      if (!response.ok) {
        return response.json().then(error => {
          throw error
        })
      }
      return response.json()
    })
    .then(data => {
      console.log(data)

      movies.value = data.movies
    })
    .catch(error => {
      console.log(error)
    })
}

onMounted(() => {
  fetchMovies()
})
</script>

<style>

.movie-img {
  width: 100%;
  height: 300px;    
  object-fit: cover;  
}
</style>