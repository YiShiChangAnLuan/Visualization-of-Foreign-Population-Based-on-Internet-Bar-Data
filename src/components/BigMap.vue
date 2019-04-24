<template>
	<!--<div id="allmap" style="width: 100%; height: {{mapHeight}}px"></div>-->
	<!--<div id="allmap":style="{width: '100%', height: mapHeight + 'px'}"></div>-->
	<div id="map" style="width: 50%;height: 100%;"></div>
</template>
<script>
	import $ from 'jquery'
	import axios from 'axios'
	import * as d3 from 'd3v4'
	export default {　　　　
		data() {　　　　　　
			return {　　　
				blackbar: ['50010210000094', '50010110000214', '50023510000012', '50024110000097', '50010110000046', '50023510000003', '50022210000107', '50011710000142', '50010510000166', '50010610007010', '50010110000030', '50023510000052', '50010510000067', '50023610000048', '50023110000004', '50011710000070', '50010210000044', '50010110000180', '50010110000176', '50011710000023', '50011710000058', '50010510000017', '50011710000159', '50010210000087', '50022210000117', '50011010000012', '50022210000021', '50010210000059', '50010510000025', '50010210000026', '50010110000016', '50010110000091', '50023610000041', '50023010000071', '50023610000003', '50010510000130', '50011710000134', '50010510000105', '50022210000013', '50010510000140', '50011710000187', '50010510000114', '50023510000001', '50010110000060', '50011710000039', '50023510000015', '50023010000059', '50010510000095', '50010510000135', '50010510000023', '50011710000030', '50010110000197', '50010510000064', '50023510000039', '50023110000062', '50010510000162', '50010110000255', '50023510000070', '50023010000029', '50023510000053', '50010610006016', '50023110000033', '50010210000049', '50011710000122', '50010110000128', '50010510000108', '50011710000107', '50023510000066', '50011710000069', '50023110000046', '50010110000249', '50010110000015', '50010110000029', '50010110000099', '50010210000041', '50023510000071', '50010110000198', '50022210000087', '50022210000120', '50010510000044', '50010110000187', '50022210000030', '50010510000146', '50023110000006', '50023610000006', '50023010000052', '50010110000145', '50010510000073', '50023110000049', '50010510000039', '50010510000136', '50010510000111', '50010510000161', '50010110000229', '50023510000023', '50011710000136', '50011010000042', '50011010000025', '50010310000279', '50023510000044', '50011010000020', '50011810000078', '50010510000101', '50010510000034', '50010210000071', '50023510000059', '50010510000193', '50010110000246', '50011710000027', '50010510000062', '50010510000141', '50022210000105', '50010510000172', '50010510000151', '50011310000170', '50011710000094', '50010510000035', '50010610005013', '50010210000073', '50023510000056', '50010110000222', '50011610000210', '50023510000010', '50022210000100', '50010510000032', '50010510000070', '50010210000079', '50023310000036', '50022210000039', '50010110000142', '50011710000064', '50010110000103', '50010610009106', '50023510000046', '50010110000218', '50022210000113', '50010210000068', '50010110000166', '50010610009061', '50010710000254', '50010110000005', '50010510000113', '50010110000235', '50010610002033', '50010510000149', '50023610000077', '50023110000031', '50023510000035', '50023110000007', '50023510000005', '50010710000281', '50010110000182', '50011710000053', '50023510000018', '50010510000092', '50010110000144', '50010210000065', '50023110000064', '50023610000018', '50022210000116', '50011710000011', '50023610000035', '50010110000162', '50010510000050', '50023510000047', '50010510000014', '50010110000260', '50011710000007', '50011010000021', '50011710000063', '50010510000076', '50011410000056', '50023110000012', '50022710000113', '50010210000004', '50010110000020', '50023610000056', '50023510000085', '50023110000025', '50022210000065', '50023110000009', '50022210000060', '50010510000071', '50011310000179', '50010110000137', '50011610000076', '50010110000160', '50023510000058', '50011010000032', '50010110000105', '50011710000092', '50010510000080', '50022210000098', '50011710000172', '50011710000018', '50023610000073', '50010210000015', '50011710000128', '50022210000045', '50010710000013', '50010510000110', '50023510000014', '50023510000074', '50010510000137', '50010210000086', '50010110000210', '50023510000027', '50010110000139', '50011210000158', '50010510000087', '50023110000041', '50010110000234', '50010510000184', '50023510000073', '50011710000043', '50010110000158', '50010510000038', '50010110000048', '50023110000040', '50022210000121', '50010710000309', '50010710000195', '50011710000163', '50010110000031', '50011710000131', '50011710000117', '50010110000008', '50023610000002', '50010510000084', '50010510000060', '50011010000038', '50010510000058', '50023510000004', '50011010000043', '50010110000159', '50022210000085', '50010510000007', '50023610000014', '50010510000078', '50010210000057', '50010110000165', '50023610000044', '50011710000050', '50011010000016', '50010210000095', '50010610001016', '50023610000023', '50023010000032', '50010510000026', '50011710000180', '50010210000036', '50010210000091', '50010110000184', '50011710000009', '50010110000186', '50023110000048', '50010510000061', '50010110000058', '50022210000115', '50010110000153', '50022210000099', '50022210000010', '50010510000169', '50010210000061', '50015310000027', '50023610000049', '50011710000171', '50023110000029', '50010510000082', '50010210000014', '50023510000082', '50022210000077', '50010110000181', '50011710000038', '50010110000156', '50010110000123', '50023110000032', '50010210000088', '50011310000164', '50023510000045', '50023610000088', '50023610000013', '50023110000071', '50010510000158', '50010710000274', '50010110000189', '50011710000093', '50010510000030', '50011710000085', '50010110000154', '50011010000014', '50023010000031', '50010510000192', '50023210000035', '50011710000095', '50011010000033', '50011710000155', '50010210000098', '50023010000067', '50011710000067', '50022210000110', '50022210000101', '50022210000016', '50010510000115', '50010210000001', '50023110000037', '50010510000121', '50022210000040', '50010510000048', '50023110000077', '50022410000071', '50011710000118', '50010510000083', '50011710000042', '50010510000004', '50010110000173', '50010110000084', '50010110000068', '50022210000102', '50010510000063', '50010510000093', '50010710000347', '50010110000041', '50023110000026', '50011010000036', '50022210000119', '50023310000058', '50023110000063', '50023110000072', '50023510000029', '50010110000196', '50022210000088', '50022210000079', '50023610000030', '50010510000065', '50022210000095', '50015310000076', '50010210000053', '50011310000079', '50010110000206', '50023210000002', '50015310000077', '50023110000069', '50010810000099', '50023610000036', '50023110000005', '50010510000200', '50010510000081', '50023510000013', '50023110000057', '50023010000011', '50011010000006', '50023510000033', '50023510000051', '50023110000053', '50010510000010', '50010510000056', '50023110000019', '50010510000132', '50011710000003', '50010510000005', '50010510000040', '50023010000002', '50011710000124', '50011010000003', '50023110000060', '50010610006004', '50010510000100', '50011710000157', '50010510000131', '50022210000057', '50010110000161', '50010510000134', '50010510000125', '50010510000187', '50023610000033', '50010510000020', '50010110000107', '50010110000120', '50010110000147', '50022210000112', '50023010000017', '50022210000104', '50010510000145', '50023610000070', '50023610000011', '50011010000044', '50010510000139', '50010610006001', '50010110000033', '50010510000112', '50010510000051', '50010110000070', '50023110000011', '50011710000006', '50023510000030', '50010610009102', '50011710000154', '50010110000150', '50010510000152', '50011610000034', '50023110000075', '50010510000138', '50011710000041', '50023610000047', '50010510000117', '50011710000175', '50023610000071', '50023610000021', '50022710000105', '50022210000051', '50010110000167', '50011410000064', '50011710000022', '50010510000052', '50023510000007', '50023110000061', '50010110000152', '50010510000106', '50023110000068', '50010210000090', '50011010000029', '50010510000133', '50010510000185', '50022210000073', '50022210000090', '50022710000002', '50011710000139', '50010510000037', '50010110000077', '50023510000002', '50023110000042', '50010110000044', '50010110000254', '50022210000108', '50010510000072', '50010210000062', '50010510000120', '50022210000071', '50010110000111', '50023610000019', '50023010000040', '50011010000040', '50011710000004', '50022210000020', '50010510000054', '50010110000258', '50010110000053', '50010310000054', '50011210000157', '50023510000067', '50010110000028', '50010510000075', '50022210000053', '50023110000067', '50010510000188', '50010510000009', '50010510000002', '50010210000011', '50010610009066', '50010110000004', '50010510000012', '50010210000067', '50023610000038', '50010110000163', '50023610000009', '50022210000011', '50023110000035', '50010110000052', '50010110000001', '50022210000076', '50023510000050', '50010510000008'],
				AllPoints: [],
				doubltbar:['50010210000001', '50022610000043', '50011010000025', '50011810000174', '50011610000206', '50010610005018', '50011610000176', '50022310000074', '50011610000078', '50023810000043', '50011810000076', '50011810000078', '50023610000044', '50023310000036', '50010710000356', '50011610000052', '50011710000166', '50011810000086', '50010610009002', '50023610000062', '50010110000082', '50010610002004', '50010110000133', '50023510000034', '50022510000050', '50011210000180', '50010310000011', '50011910000032', '50023210000031', '50011810000191', '50011710000127', '50023510000075', '50010310000029', '50022810000024', '50010610004008', '50010510000060', '50011810000184', '50010710000295', '50011610000143', '50010510000006', '50010110000244', '50022610000079', '50023110000039', '50010910000122', '50010310000187', '50022210000011', '50010310000092', '50023210000012', '50011610000051', '50010710000306', '50022710000032', '50010610006001', '50022210000003', '50011610000046', '50010610002036', '50011610000004', '50023610000002', '50011310000181', '50022610000055', '50010910000155', '50010510000082', '50011310000068', '50011810000137', '50011510000076', '50022510000071', '50023610000012', '50010710001028', '50010910000107', '50011410000055', '50011810000116', '50011610000187', '50011310000033', '50023610000013', '50011610000152', '50023610000039', '50011610000063', '50011610000166', '50010510000169', '50010510000137', '50010110000072', '50023610000064', '50010710000103', '50010510000134', '50022610000078', '50011710000039', '50011810000068', '50010510000035', '50011310000101', '50010110000103', '50011610000178', '50010810000064', '50011610000194', '50010710000259', '50011810000103', '50011510000104', '50010710000112', '50011810000180', '50010510000140', '50010610006014', '50023310000005', '50010710000266', '50022710000001', '50010310000144', '50011610000005', '50022210000087', '50011610000077', '50010210000033', '50024010000019', '50011310000113', '50022410000102', '50024210000076', '50011610000047', '50022610000056', '50023310000091', '50011610000014', '50011210000015', '50010510000052', '50023610000003', '50010510000008', '50023710000025', '50010710001051', '50022810000065', '50010510000048', '50022410000014', '50023510000064', '50010710000244', '50024210000098', '50022810000007', '50010610006003', '50010510000197', '50010510000064', '50011210000049', '50010710000226', '50011610000029', '50010610009076', '50022810000014', '50024010000047', '50010610006019', '50022710000035', '50023810000048', '50022710000007', '50022410000048', '50024210000103', '50010610009037', '50022410000098', '50010510000010', '50010610002049', '50010710000042', '50011710000142', '50023710000039', '50022510000068', '50010110000057', '50010310000071', '50010110000044', '50010610005012', '50010110000010', '50010610009113', '50010110000255', '50010810000036', '50022710000034', '50010610002030', '50022510000085', '50010610005013', '50010510000136', '50010110000102', '50011910000047', '50023610000006', '50023010000050', '50010310000107', '50010710000231', '50010110000059', '50022510000027', '50010110000137', '50023110000049', '50022510000056', '50011810000166', '50010110000218', '50023610000007', '50023410000025', '50010310000136', '50022810000066', '50010910000178', '50010710000293', '50010110000107', '50010610002018', '50011310000178', '50011510000003', '50022310000015', '50024110000122', '50023010000056', '50010310000025', '50011210000249', '50022510000002', '50010710000237', '50010610007014', '50023610000048', '50023510000063', '50024110000130', '50023310000064', '50010610007013', '50023710000069', '50011010000043', '50023710000024', '50023510000051', '50010610005019', '50011210000172', '50010210000079', '50023610000050', '50010410000059', '50022710000088', '50023610000014', '50010710000087', '50010610007015', '50011510000116', '50011610000117', '50022210000065', '50011310000024', '50011610000015', '50010510000092', '50010810000161', '50010610009081', '50022610000015', '50010510000074', '50010710000048', '50022910001008', '50022510000021', '50022810000060', '50023610000073', '50011210000016', '50015310000085', '50011610000003', '50010810000191', '50011610000048', '50010510000126', '50011510000051', '50023210000018', '50022610000017', '50010510000145', '50011810000023', '50022810000062', '50010110000225', '50011210000091', '50022410000083', '50010310000213', '50011510000119', '50023610000072', '50023610000032', '50011610000073', '50011010000030', '50010510000054', '50011610000192', '50010610009001', '50011610000135', '50010110000033', '50010710000260', '50011210000177', '50023510000041', '50011610000212', '50022310000024', '50011510000112', '50023610000034', '50023310000075', '50010610008012', '50011810000125', '50023610000018', '50010210000071', '50023510000057', '50023510000072', '50011110000023', '50010210000095', '50010110000020', '50010710001063', '50011010000029', '50011210000296', '50023410000035', '50010610009078', '50011710000120', '50023210000005', '50022410000101', '50010610002002', '50010310000007', '50024310000021', '50023310000077', '50023510000010', '50010110000238', '50010110000120', '50022610000021', '50011910000049', '50022610000036', '50023610000038', '50010710000084', '50023210000020', '50011610000158', '50011310000070', '50023610000019', '50022410000053', '50010510000149', '50022310000045', '50010710000354', '50010110000188', '50010110000006', '50022510000058', '50023610000017', '50023510000058', '50023310000081', '50011610000127', '50010110000091', '50023610000046', '50022810000035', '50011010000048', '50010110000177', '50023610000011']

			}　　　　
		},
		methods:{
			
		},
		mounted() {　　　　　　
			var me = this;
			var styleJson = [{
    "featureType": "land",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "color": "#f5f5f5ff"
    }
}, {
    "featureType": "water",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "color": "#bedbf9ff"
    }
}, {
    "featureType": "green",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "color": "#d0edccff"
    }
}, {
    "featureType": "building",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "building",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#ffffffb3"
    }
}, {
    "featureType": "building",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#dadadab3"
    }
}, {
    "featureType": "subwaystation",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "color": "#b15454B2"
    }
}, {
    "featureType": "education",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "color": "#e4f1f1ff"
    }
}, {
    "featureType": "medical",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "color": "#f0dedeff"
    }
}, {
    "featureType": "scenicspots",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "color": "#e2efe5ff"
    }
}, {
    "featureType": "highway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "weight": 4
    }
}, {
    "featureType": "highway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#f7c54dff"
    }
}, {
    "featureType": "highway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#fed669ff"
    }
}, {
    "featureType": "highway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "highway",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#8f5a33ff"
    }
}, {
    "featureType": "highway",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "highway",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "arterial",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "weight": 2
    }
}, {
    "featureType": "arterial",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#d8d8d8ff"
    }
}, {
    "featureType": "arterial",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#ffeebbff"
    }
}, {
    "featureType": "arterial",
    "elementType": "labels",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "arterial",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#525355ff"
    }
}, {
    "featureType": "arterial",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "local",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "weight": 1
    }
}, {
    "featureType": "local",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#d8d8d8ff"
    }
}, {
    "featureType": "local",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "local",
    "elementType": "labels",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "local",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#979c9aff"
    }
}, {
    "featureType": "local",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "railway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "weight": 1
    }
}, {
    "featureType": "railway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#949494ff"
    }
}, {
    "featureType": "railway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "subway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "on",
        "weight": 1
    }
}, {
    "featureType": "subway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#d8d8d8ff"
    }
}, {
    "featureType": "subway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "subway",
    "elementType": "labels",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "subway",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#979c9aff"
    }
}, {
    "featureType": "subway",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "continent",
    "elementType": "labels",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "continent",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "continent",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#333333ff"
    }
}, {
    "featureType": "continent",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "city",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "city",
    "elementType": "labels",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "city",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#454d50ff"
    }
}, {
    "featureType": "city",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "town",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "town",
    "elementType": "labels",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "town",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#454d50ff"
    }
}, {
    "featureType": "town",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "background",
    "elementType": "geometry",
    "stylers": {
        "color": "#344b58ff"
    }
}, {
    "featureType": "poilabel",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "poilabel",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "road",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "road",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}]

			//创建和初始化地图函数：
			function initMap() {
				createMap(); //创建地图
				setMapEvent(); //设置地图事件
				addMapControl(); //向地图添加控件
				addMapOverlay(); //向地图添加覆盖物
				drawControl(); //绘制自定义控件 选择网吧
				GetInitPoints(); /*获得所有经纬度信息*/
			}

			function createMap() {
				map = new BMap.Map("map");
				map.centerAndZoom(new BMap.Point(108.129609, 29.866396), 7);
			}

			function setMapEvent() {
				map.enableScrollWheelZoom();
				map.enableKeyboard();
				map.enableDragging();
				map.enableDoubleClickZoom()
				map.setMapStyle({
					styleJson: styleJson
				});
			}

			function addClickHandler(target, window) {
				target.addEventListener("click", function() {
					target.openInfoWindow(window);
				});
			}

			function addMapOverlay() {}

			//向地图添加控件
			function addMapControl() {
				var scaleControl = new BMap.ScaleControl({
					anchor: BMAP_ANCHOR_BOTTOM_LEFT
				});
				scaleControl.setUnit(BMAP_UNIT_IMPERIAL);
				map.addControl(scaleControl);
				var navControl = new BMap.NavigationControl({
					anchor: BMAP_ANCHOR_TOP_LEFT,
					type: BMAP_NAVIGATION_CONTROL_LARGE
				});
				map.addControl(navControl);
//				var overviewControl = new BMap.OverviewMapControl({
//					anchor: BMAP_ANCHOR_BOTTOM_RIGHT,
//					isOpen: true
//				});
//				map.addControl(overviewControl);
			}

			var map;
			initMap();
			map.setMapStyle({style:'midnight'});
			//var allPoint = []

			function drawControl() {
				/*自定义控件组件*/
				function ZoomControl1() {
					var wid = $("#map").width();
					var hei = $("#map").height();
					// 默认停靠位置和偏移量
					this.defaultAnchor = BMAP_ANCHOR_TOP_LEFT;
					this.defaultOffset = new BMap.Size(wid * 0.9, hei * 0.05);
				}

				function ZoomControl2() {
					var wid = $("#map").width();
					var hei = $("#map").height();
					// 默认停靠位置和偏移量
					this.defaultAnchor = BMAP_ANCHOR_TOP_LEFT;
					this.defaultOffset = new BMap.Size(wid * 0.83, hei * 0.05);
				}
				
				function ZoomControl3() {
					var wid = $("#map").width();
					var hei = $("#map").height();
					// 默认停靠位置和偏移量
					this.defaultAnchor = BMAP_ANCHOR_TOP_LEFT;
					this.defaultOffset = new BMap.Size(wid * 0.69, hei * 0.05);
				}
				
				function ZoomControl4() {
					var wid = $("#map").width();
					var hei = $("#map").height();
					// 默认停靠位置和偏移量
					this.defaultAnchor = BMAP_ANCHOR_TOP_LEFT;
					this.defaultOffset = new BMap.Size(wid * 0.74, hei * 0.05);
				}

				ZoomControl1.prototype = new BMap.Control();

				// 自定义控件必须实现自己的initialize方法,并且将控件的DOM元素返回
				// 在本方法中创建个div元素作为控件的容器,并将其添加到地图容器中
				ZoomControl1.prototype.initialize = function(map) {
					// 创建一个DOM元素
					var divGood = document.createElement("div");
					// 添加文字说明
					divGood.appendChild(document.createTextNode("正常网吧"));
					// 设置样式
					divGood.style.cursor = "pointer";
					divGood.style.border = "1px solid white";
					divGood.style.backgroundColor = "rgb(165, 204, 228)";

					// 绑定事件,点击一次绘制黑网吧
					divGood.onclick = function() {
						drawOrdinalBar();
					};

					// 添加DOM元素到地图中
					map.getContainer().appendChild(divGood);
					// 将DOM元素返回
					return divGood;
				}

				ZoomControl2.prototype = new BMap.Control();
				ZoomControl2.prototype.initialize = function(map) {
					var divBad = document.createElement("div");
					// 添加文字说明
					divBad.appendChild(document.createTextNode("黑网吧"));
					// 设置样式
					divBad.style.cursor = "pointer";
					divBad.style.border = "1px solid white";
					divBad.style.backgroundColor = "#f18576";
					// 绑定事件,点击一次放大两级
					divBad.onclick = function() {
						drawBlackBar()
					}

					// 添加DOM元素到地图中
					map.getContainer().appendChild(divBad);
					// 将DOM元素返回
					return divBad;
				}
				
				// 12/14 zy 新加重新绘制所有点
				ZoomControl3.prototype = new BMap.Control();
				ZoomControl3.prototype.initialize = function(map) {
					// 创建一个DOM元素
					var divall = document.createElement("div");
					// 添加文字说明
					divall.appendChild(document.createTextNode("全部"));
					// 设置样式
					divall.style.cursor = "pointer";
					divall.style.border = "1px solid white";
					divall.style.backgroundColor = "rgb(165, 204, 228)";

					// 绑定事件,点击一次绘制黑网吧
					divall.onclick = function() {
						map.clearOverlays();
						var locat1 = me.AllPoints.filter(function(d) {return me.blackbar.indexOf(d['SITEID']) == -1;})
						drawPoints(locat1)
						var locat2 = me.AllPoints.filter(function(d) { return me.blackbar.indexOf(d['SITEID']) != -1; })  
						drawPoints(locat2);
					};

					// 添加DOM元素到地图中
					map.getContainer().appendChild(divall);
					// 将DOM元素返回
					return divall;
				}
				
				ZoomControl4.prototype = new BMap.Control();
				ZoomControl4.prototype.initialize = function(map) {
					var divDoublt = document.createElement("div");
					// 添加文字说明
					divDoublt.appendChild(document.createTextNode("嫌疑黑网吧"));
					// 设置样式
					divDoublt.style.cursor = "pointer";
					divDoublt.style.border = "1px solid white";
					divDoublt.style.backgroundColor = "#B4CDCD";
					//divDoublt.style.color="white"
					// 绑定事件,点击一次放大两级
					divDoublt.onclick = function() {
						drawDoubltBar()
					}

					// 添加DOM元素到地图中
					map.getContainer().appendChild(divDoublt);
					// 将DOM元素返回
					return divDoublt;
				}
				
				// 创建控件
				var myZoomCtrl1 = new ZoomControl1();
				var myZoomCtrl2 = new ZoomControl2();
				var myZoomCtrl3 = new ZoomControl3();
				var myZoomCtrl4 = new ZoomControl4();
				// 添加到地图当中
				map.addControl(myZoomCtrl1);
				map.addControl(myZoomCtrl2);
				map.addControl(myZoomCtrl3);
				map.addControl(myZoomCtrl4);
			}

			function GetInitPoints() {
				d3.csv(('../../static/data/NetBarInfo.csv'), function(error, info) {
					if(error) {
						console.log(error);
					}
					console.log(info)
					me.AllPoints = info;
					drawPoints(me.AllPoints);
				})
			}

			function initPoints(points, options) {
				var pointCollection = new BMap.PointCollection(points, options); // 初始化PointCollection
				pointCollection.addEventListener('click', function(e) {
					var SITEID = "";
					var TITLE = "";
					for(var i = 0; i < me.AllPoints.length; i++) {
						//points.push(new BMap.Point(info[i].lng, info[i].lat));
						if(me.AllPoints[i].lng == e.point.lng && me.AllPoints[i].lat == e.point.lat) { //经度==点击的,维度
							SITEID = me.AllPoints[i].SITEID;
							TITLE = me.AllPoints[i].TITLE;
							//console.log(SITEID)
							me.$root.Bus.$emit('BarSurfHabits', SITEID)
							me.$root.Bus.$emit('calendar', SITEID)
							break;
						}
					}
					var point = new BMap.Point(e.point.lng, e.point.lat);
					var opts = {
						// width: 250, // 信息窗口宽度
						// height: 70, // 信息窗口高度
						title: "", // 信息窗口标题
						enableMessage: false, //设置允许信息窗发送短息
					}
					var infowindow = new BMap.InfoWindow("SITEID：" + SITEID + "<br/>TITLE：" + TITLE, opts);
					map.openInfoWindow(infowindow, point);
				});
				map.addOverlay(pointCollection); // 添加Overlay
			}

			function drawBlackBar() {
				//console.log("black")
				var locat = me.AllPoints.filter(function(d) {
					return me.blackbar.indexOf(d['SITEID']) != -1;
				})
				// 12/14 zy 新加绘制黑网吧点前 清楚所有点
				//map.clearOverlays();
				drawPoints(locat);
			}

			function drawOrdinalBar() {
				var locat = me.AllPoints.filter(function(d) {
					return me.blackbar.indexOf(d['SITEID']) == -1 && me.doubltbar.indexOf(d['SITEID']) == -1;
				})
				// 12/14 zy 新加绘制网吧点前 清楚所有点
				map.clearOverlays();
				drawPoints(locat);
			}
			
			function drawDoubltBar() {
				var locat = me.AllPoints.filter(function(d) {
					return me.doubltbar.indexOf(d['SITEID']) != -1 && me.blackbar.indexOf(d['SITEID']) == -1;
				})
				// 12/14 zy 新加绘制黑网吧点前 清楚所有点
				//map.clearOverlays();
				drawPoints(locat);
			}

			function drawPoints(info) {
				if(document.createElement('canvas').getContext) { // 判断当前浏览器是否支持绘制海量点
					var pointsGood = []; // 添加海量点数据
					var pointsBad = [];
					var pointsDoublt=[];
					for(var i = 0; i < info.length; i++) {
						if(me.blackbar.indexOf(info[i]['SITEID']) != -1) {
							pointsBad.push(new BMap.Point(info[i].lng, info[i].lat));
						} else if(me.doubltbar.indexOf(info[i]['SITEID']) != -1){
							pointsDoublt.push(new BMap.Point(info[i].lng, info[i].lat));
						}
						else{
							pointsGood.push(new BMap.Point(info[i].lng, info[i].lat));
						}
					}

					////console.log(pointsGood)
					////console.log(pointsBad)
					var optionsGood = {
						size: BMAP_POINT_SIZE_SMALL,
						shape: 1,
						color: 'rgb(120, 160,200)'
					}
					var optionsBad = {
						size: BMAP_POINT_SIZE_SMALL,
						shape: 0,
						color: '#B22222'
					}
					
					var optionsDoublt={
						size: BMAP_POINT_SIZE_SMALL,
						shape: 0,
						color: '#B4CDCD'
					}
					
					initPoints(pointsGood, optionsGood);
					initPoints(pointsBad, optionsBad);
					initPoints(pointsDoublt, optionsDoublt);
				} else {
					alert('请在chrome、safari、IE8+以上浏览器查看本示例');
				}
			}

			function PointToBars(barid) {
				map.clearOverlays();

				//console.log(me.AllPoints)
				var locat = me.AllPoints.filter(function(d) {
					return barid.indexOf(d['SITEID']) != -1;
				})
				console.log(locat);
				//console.log(location[0]['lng'],location[0]['lat'])
				map.panTo(new BMap.Point(parseFloat(locat[0]['lng']), parseFloat(locat[0]['lat'])));
				drawPoints(locat)
			}

			this.$root.Bus.$on('yichangBar', function(barid) {
				PointToBars(barid);
			});
		}　　
	}
</script>

<style>
/*去掉百度地图的logo*/
.anchorBL{
  display: none;
}
</style>