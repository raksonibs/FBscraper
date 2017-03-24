require 'sequel'
require "csv"

# Run time argv
DB = Sequel.connect("sqlite://fb.sqlite")

# Load to_csv method via extension
DB.extension(:sequel_3_dataset_methods)

CSV.open("output.csv", "w") do |csv|
  csv << ["person_hash_id", "person_id", "person_name"]

  DB['SELECT * FROM People;'].each do |person|
    csv << [person[:person_hash_id], person[:person_id], person[:person_name]]
  end
end
