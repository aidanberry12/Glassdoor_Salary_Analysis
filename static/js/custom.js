function getOption() {
			// load selections from HTML controls into JS variables
			selectElementTitle = document.querySelector('#title');
			selectElementSector = document.querySelector('#sector');
			selectElementRegion = document.querySelector('#region');



			// load the values selected for the scoring parameters into JS variables
			title_string = selectElementTitle.options[selectElementTitle.selectedIndex].value;
			sector_string = selectElementSector.options[selectElementSector.selectedIndex].value;
			region_string = selectElementRegion.options[selectElementRegion.selectedIndex].value;

      console.log(title_string, sector_string, region_string);
      //drop_down_dict = {"title": title_string, "sector":sector_string, "region_string":region_string}
		}
