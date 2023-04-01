const fs = require('fs');

module.exports = function readDatabase(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
            if (err) return reject(Error('Cannot load the database'));
            // split data and gets only list without header
            const lines = data.split('\n').slice(1, -1);
            // provide header of data
            const header = data.split('\n').slice(0, 1)[0].split(',');
            // find firstname and index
            const idxFn = header.findIndex((ele) => ele === 'firstname');
            const idxFd = header.findIndex((ele) => ele === 'field');
            const fields = {};
            const students = {};
            // contain all data
            const all = {};

            lines.forEach((line) => {
                const list = line.split(',');
                if (!fields[list[idxFd]]) fields[list[idxFd]] = 0;
                fields[list[idxFd]] += 1;
                if (!students[list[idxFd]]) students[list[idxFd]] = '';
                students[list[idxFd]] += students[list[idxFd]]
                    ? `, ${list[idxFn]}`
                    : list[idxFn];
            });
            for (const key in fields) {
                if (Object.hasOwnProperty.call(fields, key)) {
                    const number = fields[key];
                    all[key] = {
                        students: `List: ${students[key]}`,
                        number,
                    };
                }
            }

            return resolve(all);
        });
    });
};
