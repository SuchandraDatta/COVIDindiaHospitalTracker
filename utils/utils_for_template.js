augment_template = (data, insert_data_in_template) =>
{
	/*
	Input: data which is the HTML code as a large string and insert_data_in_template which is a JSON containing the data to be entered.

	Output: returns the HTML code, replacing the { in template with the data that is supposed to be placed their for dynamic display.

	*/
	//step1 is extract the template which is everything between @ and @ in main.html. Template is just the div with card-layout that's gonna be repeated.
	let step1 = get_start_and_end_indices(data, "@")
	let extracted_template = data.substring(step1[0], step1[1])
	let extracted_template_copy = extracted_template
	//Keep a copy of this template format as the format is updated with new data in each iteration of for loop.

	let data_to_be_output = JSON.parse(insert_data_in_template)//The data passed was a string
	let part_one = data.substring(0, step1[0]-1)//All HTML code before template enclosed in @@
	let part_two = data.substring(step1[1]+1)//All HTML code after the closing @
	let final_output = ""
	for (item in data_to_be_output)
	{
		for(key in data_to_be_output[item])
		{
			step2 = get_start_and_end_indices(extracted_template, "{")//{ opening curly braces marks the spot where data is to be inserted, here the state name and beds available value. The opening { must have a space before and after it.
			replace_brackets_with_this = data_to_be_output[item][key]
			extracted_template = extracted_template.substring(0, step2[0]-1) + replace_brackets_with_this + extracted_template.substring(step2[0]+1)
			step2 = extracted_template
			//console.log("replace_brackets_with_this ", replace_brackets_with_this)
		}
		final_output = final_output + extracted_template
		extracted_template = extracted_template_copy
	}

	final_output = part_one + final_output + part_two
	return final_output

}
get_start_and_end_indices = (data, symbol) =>
{
	/*
	Input: data, which is a string and symbol, whose index is to be found out.
	Output: Returns a list of 2 items, item[0] is the first index at which symbol is present + 1, item[1] is the last index at which symbol is present. Symbol is usually @ or { symbol. 
	*/
	return [ data.indexOf(symbol)+1, data.lastIndexOf(symbol)]
}

module.exports= {
	"augment_template":augment_template,
}