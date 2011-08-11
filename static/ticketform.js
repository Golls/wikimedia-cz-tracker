function refresh_description()
{
	var topic_id = $('#id_topic').val();
	if (topic_id == '')
	{
		$('#topic_desc').hide();
		$('#mediainfo-group').hide();
	}

	var topic = topics_table[topic_id];
	$('#topic_desc').html(topic['form_description']).toggle(topic['form_description'] != "");
	$('#mediainfo-group').toggle(topic['detailed_tickets']);
}

$(document).ready(function() {
	$('#id_topic').change(refresh_description);
	refresh_description();
});
