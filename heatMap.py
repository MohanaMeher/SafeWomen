import gmplot 
  
latitude_list = [ 12.934310, 12.926936, 12.924864] 
longitude_list = [77.622603,  77.629506, 77.630029 ] 
  
gmap = gmplot.GoogleMapPlotter(12.928494, 
                                77.627615, 13) 
  
gmap.scatter( latitude_list, longitude_list, '# FF0000', 
                                size = 40, marker = False) 
  
gmap.heatmap(latitude_list, longitude_list) 
  
gmap.draw( "index.html" ) 