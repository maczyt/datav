const mysql = require('mysql');
const path = require('path');
const fs = require('fs-extra');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'lagou'
});

connection.connect((err) => {
  if (err) {
    console.error('链接失败: ', err);
    return;
  }
  console.log('链接成功')
});

/**
 * 查询行业信息
 */
function query_industryField_result() {
  const name = '行业信息';
  const column = 'industryField';
  common_query(name, column);
}

/**
 * 查询薪资情况
 */
function query_salary_result() {
  const name = '薪资情况';
  const column = 'salary';
  common_query(name, column);
}

/**
 * 查询工作年限
 */
function query_workyear_result() {
  const name = '工作年限';
  const column = 'workYear';
  common_query(name, column);
}

/**
 * 查询学历信息
 */
function query_education_result() {
  const name = '学历信息';
  const column = 'education';
  common_query(name, column);
}

/**
 * 根据城市计数
 */
function query_city_result() {
  const name = '根据城市计数';
  const column = 'city';
  common_query(name, column);
}

/**
 * 融资情况
 */
function query_financeStage_result() {
  const name = '融资情况';
  const column = 'financeStage';
  common_query(name, column);
}

/**
 * 公司规模
 */
function query_companySize_result() {
  const name = '公司规模';
  const column = 'companySize';
  common_query(name, column);
}

/**
 * 任职情况
 */
function query_jobNature_result() {
  const name = '任职情况';
  const column = 'jobNature';
  common_query(name, column);
}

/**
 * 岗位数量
 */
function query_job_result() {
  connection.query('select COUNT(*), crawl_date from lagou_data', (err, res) => {
    if (err) {
      console.log('查询岗位数量失败')
      return;
    }
    const result_lit_map = res.map(item => {
      return {
        name: item['crawl_date'],
        value: item['COUNT(*)'],
      }
    });
    const file = path.resolve('./tmp/job.json');
    fs.writeJSONSync(file, result_lit_map)
  });  
} 

/**
 * 抓取数量
 */
function query_count_result() {
  connection.query('select COUNT(*) from lagou_data', (err, res) => {
    if (err) {
      console.log('查询抓取数量失败')
      return;
    }
    const map = res[0];
    const result_lit_map = {
      allCount: map['COUNT(*)'],
      todayCount: map['COUNT(*)'],
    };
    const file = path.resolve('./tmp/count.json');
    fs.writeJSONSync(file, result_lit_map);
  });  
}
query_industryField_result();
query_salary_result();
query_workyear_result();
query_education_result();
query_job_result();
query_city_result();
query_financeStage_result();
query_companySize_result();
query_jobNature_result();
query_count_result();
connection.end();

/**
 * 统计
 * @param {*} arr 
 */
function counter(arr) {
  return arr.reduce((m, item) => {
    m[item] = m[item] ? m[item] + 1 : 1;
    return m;
  }, {});
}

/**
 * 公共查询方法
 * @param {*} name 
 * @param {*} column 
 */
function common_query(name, column) {
  connection.query(`select ${column} from lagou_data`, (err, res) => {
    if (err) {
      console.log(`查询${name}失败`)
      return;
    }
    const result_list = res.map(item => {
      if (item[column].indexOf(',') !== -1) {
        return item[column].split(',')[0];
      }
      return item[column];
    });
    const result_map = counter(result_list);
    const result_lit_map = Object.keys(result_map).map(key => {
      return {
        name: key,
        value: result_map[key],
      }
    });
    const file = path.resolve(`./tmp/${column}.json`);
    fs.writeJSONSync(file, result_lit_map);
  });  
}