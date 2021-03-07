//https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.7.4+commit.3f05b770.js
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.8.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 */
contract DriverLicense {

    enum LicenseStatus { Expired, Valid }
    LicenseStatus public status;

    mapping(uint256 => License) public licences;
    mapping(uint256 => uint256) public indexes;
    uint256 public count = 0;
    uint256 internal day = 86400;

    address owner;
    uint256 validatedIn = 1613820891;

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    // modifier onlyWhileOpen() {
    //     require(block.timestamp <= licences[id].expiration);
    //     _;
    // }

    struct License {
        string firstName;
        string lastName;
        uint256 id;
        uint256 expiration;// = block.timestamp + x(days)
    }

    constructor() public {
        owner = msg.sender;
    }

    function addDrivingLicence(
        string  memory _firstName,
        string  memory _lastName,
        uint256 _id,
        uint256 _expiration
        )
        public
        onlyOwner
    {
        uint256 expiration_date = block.timestamp + (day * _expiration);
        incrementCount();
        indexes[count] = _id;
        licences[_id] = License(_firstName, _lastName, _id, expiration_date);
    }

    function incrementCount() internal {
        count++;
    }

    // function getAllLicenses() public onlyOwner{
    //     for (uint256 i = 0; i < count; i++) {
    //         licences[indexes[i]].firstName;
    //         licences[indexes[i]].lastName;
    //         licences[indexes[i]].id;
    //         licences[indexes[i]].expiration;
    //     }
    // }

    function isOwner() public returns(bool) {
        return msg.sender == owner;
    }

    function updateExpiration(uint256 _id, uint256 _expiration) public onlyOwner {
        licences[_id].expiration = block.timestamp + (day * _expiration);
    }

    // function getLicense(uint256 _id) public view returns(License memory) {
    //     License memory result = licences[_id];
    //     return result;
    // }
}