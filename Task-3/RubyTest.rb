#! /usr/bin/env ruby

require 'nokogiri'
require 'open-uri'

# Fetch and parse HTML document
doc = Nokogiri::HTML(open('https://www.wix.com/blog/2018/08/blog-examples/'))

doc.css('nav ul.menu li a', '//article//h2').each do |link|
  puts link.content
end

doc.xpath('//nav//ul//li/a', '//article//h2').each do |link|
  puts link.content
end

doc.search('nav ul.menu li a', '//article//h2').each do |link|
  puts link.content
end
