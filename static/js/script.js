document.addEventListener('DOMContentLoaded', function () {
  // Materialize required JS for the mobile sidenav
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, {edge: "right"});

  // Materialize required JS for the Forms 'select' function
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems, {});

  // Materialize required JS for the delete recipe modal
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems, {});
});