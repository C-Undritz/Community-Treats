/*
Required Javascript for Materialize features to work as expected (https://materializecss.com/)
*/

document.addEventListener('DOMContentLoaded', function () {
  // Materialize required JS for the mobile sidenav
  var elems_sidenav = document.querySelectorAll('.sidenav');
  var instances_sidenav = M.Sidenav.init(elems_sidenav, {edge: "right"});

  // Materialize required JS for the Forms 'select' functions
  var elems_form = document.querySelectorAll('select');
  var instances_form = M.FormSelect.init(elems_form, {});

  // Materialize required JS for the modals
  var elems_modal = document.querySelectorAll('.modal');
  var instances_modal = M.Modal.init(elems_modal, {});

  // Materialize required JS for the tool-tips
  var elems_tooltip = document.querySelectorAll('.tooltipped');
  var instances_tooltip = M.Tooltip.init(elems_tooltip, {margin: 0, enterDelay: 600});

  // Meterialize required JS for the collapsible within the admin gudie
  var elems_collapsible = document.querySelectorAll('.collapsible');
  var instances_collapsible = M.Collapsible.init(elems_collapsible, {});
});