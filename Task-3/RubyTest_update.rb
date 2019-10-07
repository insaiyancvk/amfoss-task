#!/usr/bin/ruby

require 'nokogiri'
require 'open-uri'

puts "Enter the search word"
search = gets

link = "https://www.google.com/search?num=10&q="

doc = Nokogiri:: HTML(open(link+search))

s = doc.xpath('//a/div').each do |results|
     puts results.text
end