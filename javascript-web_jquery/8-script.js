$.get("https://swapi-api.hbtn.io/api/people/5/?format=json", (data) => {
  const arr = data.films;
  arr.forEach((elem) => {
    $.get(elem, (data) => {
      const item = $("<LI></LI>").text(data.title);
      $("#list_movies").append(item)
    })
  })
})