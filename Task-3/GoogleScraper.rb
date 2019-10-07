require 'nokogiri'
require 'open-uri'
require 'pry'
require 'ruby-progressbar'

puts "Enter a search phrase"
search = gets

array = Array.new(1001)
progressbar = ProgressBar.create(:total => array.size)

array.each do |item|
    progressbar.increment
    sleep 0.005
end

doc = Nokogiri::HTML(open('https://www.google.com/search?num=11&q='+search))

doc.xpath('//a/div[@class="BNeawe vvjwJb AP7Wnd"]').each do |r|
    puts ""
    puts r.text
end
