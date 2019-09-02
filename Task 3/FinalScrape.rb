#!/usr/bin/ruby

require 'nokogiri'
require 'open-uri'

puts "\nEnter the search text :"
search = gets

puts "\nThe search results :"
puts ""

doc = Nokogiri:: HTML(open("https://www.google.com/search?num=10&q="+search))

s = doc.xpath('//a/div').each do |results|
    puts results.text
    puts ""
end